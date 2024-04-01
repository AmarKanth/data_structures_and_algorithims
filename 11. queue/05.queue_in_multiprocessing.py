from multiprocessing import Queue

q = Queue(maxsize=3)
print(q.put(1))
print(q.get())
print(q.qsize())