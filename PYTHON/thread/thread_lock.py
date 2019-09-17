#coding=utf-8
import threading
import time

# create a mutex
mutex = threading.Lock()
# locking
# mutex.acquire()

# unlocking
# mutex.release()

def saySorryMeal():
	# mutex.acquire()
	for i in range(5):
		print("Honey, I was wrong, can I have my meal?")
		time.sleep(1)
	# mutex.release()

def saySorryMoney():
	# mutex.acquire()
	for i in range(5):
		print("Hsoney, I was wrong, can I have my money?")
		time.sleep(1)
	# mutex.release()	

def main():
	t1 = threading.Thread(target = saySorryMeal)
	t2 = threading.Thread(target = saySorryMoney)
	t1.start()
	t2.start()

	time.sleep(1)

	print(threading.enumerate())

if __name__ == "__main__":
	main()