from queue import Queue

q = Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())
print(q.empty())
print(q.full())
print(q.get())