import socket
def main():
	host = '10.1.132.64'
	port = 5004
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, address = s.accept()
	print('connection from ' + str(address))
	while True:
		data = c.recv(1024)
		if not data:
			break
		print('from connected user ' + str(data.decode()))
		data = str(data.decode()).upper()
		print('sending: ' + str(data))
		c.send(data.encode())
	c.close()
if __name__ == '__main__':
	main()

