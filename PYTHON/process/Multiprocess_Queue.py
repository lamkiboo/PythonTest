import multiprocessing

def download_from_web(q):
	# 模拟下载数据
	data = [11, 22, 33, 44]

	# 向队列中写入数据
	for temp in data:
		if not q.full():
			q.put(temp)

	print("___已经下载数据完毕，等待解析___\r\n")

def analysis_data(q):
	waitting_analysis_data = list()
	while True:
		data = q.get()
		waitting_analysis_data.append(data)

		if q.empty():
			break
	print(waitting_analysis_data)

def main():
	# 1 创建一个队列 (进程池创建队列需要用Manager.Queue)
	q = multiprocessing.Queue()

	# 2 创建多个进程
	P_down = multiprocessing.Process(target = download_from_web, args = (q,))
	P_ana = multiprocessing.Process(target = analysis_data, args = (q,))

	P_down.start()
	P_ana.start()

if __name__ == "__main__":
	main()