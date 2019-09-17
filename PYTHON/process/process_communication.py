import multiprocessing
from multiprocessing import Queue

# 初始化一个Queue对象 最多接受三条put消息
q = multiprocessing.Queue(3)

q.put("消息1")
q.put("消息1")

print(q.full())  # False

q.put("消息3")

print(q.full())  # True


# 因为消息队列已满 以下的try都会抛异常 第一个try会等待两秒抛异常 第二个立即抛异常
try:
	q.put("消息4", True, 2)
except:
	print("消息队列已满，现有消息数量:%s" %q.qsize())


try:
	q.put_nowait("消息4")
except:
	print("消息队列已满，现有消息数量:%s" %q.qsize())

# 推荐方式 先判断消息队列是否已满 再写入
if not q.full():
	q.put_nowait("消息4")

# 读取消息时 先判断消息队列是否为空 再进行读取
if not q.empty():
	for i in range(q.qsize()):
		print(q.get_nowait())