import socket
def main():
	dollar = {'INR': 67.0, 'yern': 113.41, 'pounds': 0.75}
	INR = {'dollar': 0.014, 'yern': 1.58 , 'pounds': 0.11}
	pounds = {'dollar': 1.26, 'yern': 142 , 'INR': 90.0}
	yern = {'dollar': 0.0089 , 'INR': 0.63 , 'pounds': 0.007}
	host  = '10.10.9.59'
	lst = [dollar, INR, pounds, yern]
	port = 5200
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, address = s.accept()
	print('connection from ' + str(address))
	while True:
		data = c.recv(1024)
		data = str(data.decode()).split()
		if data[1] == 'dollar':
			result = float(dollar.get(data[4]) * int(data[2]))
		elif data[1] == 'INR':
			result = float(INR.get(data[4]) * int(data[2]))
		elif data[1] == 'yern':
			result = float(yern.get(data[4]) * int(data[2]))
		elif data[1] == 'pounds':
			result = float(pounds.get(data[4]) * int(data[2]))
		print('sending:' + str(result))
		c.send(str(result).encode())
	c.close()
if __name__ == '__main__':
	main()
