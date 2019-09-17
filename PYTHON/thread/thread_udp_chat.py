import socket
import threading
import time

def recv_msg(udp_socket):
	"""recieve messege and show on"""
	while True:
		recv_data = udp_socket.recvfrom(1024)
		print(recv_data)

def send_msg(udp_socket, dest_ip, dest_port):

	while  True:
		send_data = input("Please input the sending messege\r\n")
		udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def main():
	
	# 1.creat socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 2.bind local messege
	udp_socket.bind(("", 7890))

	# 3.get the ip
	dest_ip = input("Please input the ip\r\n")
	dest_port = int(input("Please input the port\r\n"))

	# 4.creat 2 thread
	t_recv = threading.Thread(target = recv_msg, args = (udp_socket,))
	t_send = threading.Thread(target = send_msg, args = (udp_socket, dest_ip, dest_port))

	t_recv.start()
	t_send.start()

if __name__ == "__main__":
	main()
