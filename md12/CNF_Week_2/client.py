import socket
from _thread import *
from threading import *
import threading
# def receive(s, username):
# 	while True:
# 		data = s.recv(1024).decode()
# 		if not data:
# 			continue
def main():
	host = '10.10.9.59'
	port  = 8070
	s = socket.socket()
	s.connect((host, port))
	username = input()
	s.send(username.encode())
	# Thread(target = receive, args = (s,username)).start()
	message = s.recv(1024).decode()
	if message == 'rollnumber not found':
		print(message)
		return
	while True:
		msg = s.recv(1024).decode()
		print(msg)
		answer = input()
		s.send(answer.encode())
	return
	s.close()

if __name__ == '__main__':
	main()



