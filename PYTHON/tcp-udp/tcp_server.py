import socket

def main():
	# creat a tcp socket
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_ip = input("Please Input the Server-IP:")
	server_port = int(input("Please Input the Server-PORT:"))

	# bind the local port
	tcp_server_socket.bind((server_ip, server_port))

	# wait for being connected 
	# listen(128): there is allowed 128 clients connected at the same time
	tcp_server_socket.listen(128)
	clinet_socket, client_Addr = tcp_server_socket.accept()

	# use socket send/recieve data
	while True:

		recvData = clinet_socket.recv(1024)
		print('Recieve Data:', recvData.decode('gbk'))

		send_data = input("please input send data:")

		if send_data == "exit":
			break

		clinet_socket.send(send_data.encode("gbk"))

		

	# close socket
	tcp_server_socket.close()

	print("______done______")


if __name__ == '__main__':
	main()