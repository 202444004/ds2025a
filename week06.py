from queue import Queue


q = Queue()
q.put("DataStructure")
q.put("DataBase")
q.put("JavaScript")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
