import socket
import csv
from _thread import *
from threading import *
def clientthread(conn, addr):
	user = conn.recv(1024).decode()
	if user in student_dict.keys():
		while True:
			conn.send('rollnumber found'.encode())
			for key in student_dict:
				if key == user:
					conn.send(student_dict[key].encode())
					answer = conn.recv(1024).decode()
					if student_ans[key] == answer:
						conn.send('attendance: present'.encode())
	else:
		conn.send('rollnumber not found'.encode())
		conn.close()
	conn.close()

student_dict = {}
student_ans = {}
with open('data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	count = 10
	for row in csv_reader:
			student_ans[row[0]] = row[2]
			student_dict[row[0]] = row[1]
host = '10.10.9.59'
port = 8070
s = socket.socket()
s.bind((host, port))
print('server is ready')
s.listen(10)
while True:
	conn, addr = s.accept()
	print(str(addr) + 'connected:')
	Thread(target = clientthread, args = (conn, addr)).start()
conn.close()
s.close()



