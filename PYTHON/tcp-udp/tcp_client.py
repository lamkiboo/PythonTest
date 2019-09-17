import socket

def main():
	# creat a tcp socket
	tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_ip = input("Please Input the Server-IP:")
	server_port = int(input("Please Input the Server-PORT:"))

	# connect the server
	tcp_client_socket.connect((server_ip, server_port))

	# use socket send/recieve data
	while True:
		send_data = input("please input send data:")

		if send_data == "exit":
			break
		#udp_socket.sendto(b"hello world", dest_addr)
		tcp_client_socket.send(send_data.encode("gbk"))

		recvData = tcp_client_socket.recv(1024)
		print('Recieve Data:', recvData.decode('gbk'))

	# close socket
	tcp_client_socket.close()

	print("______done______")


if __name__ == '__main__':
	main()