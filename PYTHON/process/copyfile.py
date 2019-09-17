from multiprocessing import Manager, Pool
import os, time, random

def copy_file(queue, file_name, old_folder_name, new_folder_name):
	"""完成文件的copy"""
	old_f = open(old_folder_name + "/" + file_name, "rb")
	content = old_f.read()
	old_f.close()

	new_f = open(new_folder_name + "/" +file_name, "wb")
	new_f.write(content)
	new_f.close()

	# 拷贝完文件 向队列中写入消息 表示完成
	queue.put(file_name)

def main():
	# 获取用户要copy的文件名
	old_folder_name = input("请输入要copy的文件夹名字:")

	# 创建一个新的文件夹
	try
		new_folder_name = old_folder_name + "[副本]"
		os.mkdir(new_folder_name)
	except:
		pass

	# 获取文件夹内所有的待copy的文件名 listdir()
	file_names = os.listdir(old_folder_name)
	file_nums = len(file_names)

	# 创建进程池
	po = multiprocessing.Pool(5)

	# 创建队列
	q = multiprocessing.Manager().Queue()

	# 向进程池中添加拷贝文件的任务
	for file_name in file_names:
		po.apply_async(copy_file, args = (q, file_name, old_folder_name, new_folder_name))

	po.close()
	# po.join()

	file_copy_cont = 0

	# 进度条显示
	while True:
		file_name = q.get()
		file_copy_cont++
		print("\r拷贝进度:%.1f%%" % (100 * file_copy_cont/file_nums), end = "")

		if file_copy_cont >= file_nums:
			print("\r\n")
			break


	# copy原文件夹中的文件 到新的文件夹中去

if __name__ == "__main__":
	main()