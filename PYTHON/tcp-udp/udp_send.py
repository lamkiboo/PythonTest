import socket

def main():
	# creat a udp socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# use socket send data
	dest_addr = ('192.168.1.202', 8080)
	while True:
		send_data = input("please input send data")

		if send_data == "exit":
			break
		#udp_socket.sendto(b"hello world", dest_addr)
		udp_socket.sendto(send_data.encode("utf-8"), dest_addr)

	# close socket
	udp_socket.close()

	print("______done______")


if __name__ == '__main__':
	main()
