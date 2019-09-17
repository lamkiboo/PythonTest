import socket
import sys

def send_file_2_client(new_client_socket, client_addr):
	# recieve the file name
	file_name = new_client_socket.recv(1024).decode("utf-8")
	print("client(%s) needs to download the flie: %s" % (str(client_addr), file_name))

	file_content = None
	try:
		f =  open(file_name, "rb")
		file_content = f.read()
		f.close()
	except Exception as ret:
		print("there is no file named:%s" % file_name)

	# send data to client
	if file_content:
		new_client_socket.send(file_content)

def main():
	# creat the socket
	tcp_server_socket = socket(socket.AF_INET, socket.SOCK_STREAM)
	# local messege
	server_ip = input("Please Input the Server-IP:")
	server_port = int(input("Please Input the Server-PORT:"))

	# bind the local port and start to listen
	tcp_server_socket.bind((server_ip, server_port))
	tcp_server_socket.listen(128)

	while True:
		# wait for being connected
		new_client_socket, client_addr = tcp_server_socket.accept()

		# use function to send file to client
		send_file_2_client(new_client_socket, client_addr)
	
		# close socket
		new_client_socket.close()
		
	tcp_server_socket.close()


if __name__ == '__main__':
	main()