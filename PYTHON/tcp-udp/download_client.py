import socket
import sys

def main():

	# creat the socket
	tcp_client_socket = socket(socket.AF_INET, socket.SOCK_STREAM)
	# local messege
	server_ip = input("Please Input the Server-IP:")
	server_port = int(input("Please Input the Server-PORT:"))

	# connect the server
	tcp_client_socket.connect((server_ip, server_port))
	
	# input the downloading file name
	file_name = input("Please input the downloading file name:")

	# send the downloading request
	tcp_client_socket.send(file_name.encode("utf-8"))

	# recieve the data (1MB)
	recv_data = tcp_client_socket.recv(1024*1024)

	# write data into the local file in binary system(wb)
	if recv_data:
		with open("[recieve]" + file_name, "wb") as f:
			f.write(recv_data)

	# close the socket
	tcp_client_socket.close()


if __name__ == '__main__':
	main()