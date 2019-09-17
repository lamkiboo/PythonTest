#coding=utf-8
import threading
import time

def saySorry(mod):
	if mod == 1:
		for i in range(5):
			print("Honey, I was wrong, can I have my meal?")
			time.sleep(1)

	if mod == 2:
		for i in range(5):
			print("Honey, I was wrong, can I have my money?")
			time.sleep(1)	

sorry_mod = [1]

def main():
	t = threading.Thread(target = saySorry, args = (sorry_mod,))
	t.start()

	print(threading.enumerate())

if __name__ == "__main__":
	main()