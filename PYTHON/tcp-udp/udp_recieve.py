import socket

def main():
	# creat a udp socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# bind local port
	local_addr = ('', 1215)
	udp_socket.bind(local_addr)

	# use socket recieve data
	while True:
		rev_data = udp_socket.recvfrom(1024)
		rev_msg = rev_data[0]
		send_addr = rev_data[1]

		if rev_msg.decode('gbk') == "exit":
			break
		
		print("%s:%s" % (str(send_addr), rev_msg.decode('gbk')))

	# close socket
	udp_socket.close()

	print("______done______")


if __name__ == '__main__':
	main()
