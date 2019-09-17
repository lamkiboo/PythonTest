from multiprocessing import Pool
import os, time, random

def worker(msg):
	t_start = time.time()
	print("%s 开始执行 进程号为%d\r\n" % (msg, os.getpid()))
	# 随机生成0-1的随机浮点数
	time.sleep(random.random() * 2)
	t_stop = time.time()
	print(msg, "执行完毕 消耗时间%0.2f\r\n" % (t_stop - t_start))

def main():
	# 创建最多3个进程的进程池
	po = Pool(3)

	for i in range(0, 10):

		po.apply_async(worker, (i, ))

	print("---start---\r\n")
	po.close()  # 关闭进程池 关闭后po不再接受新的请求
	po.join()  # 等待po中所有子进程执行完成 必须放在close后
	print("---stop---\r\n")


if __name__ == "__main__":
	main()
