class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class Quene:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enquene(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

q = Quene()
q.enquene("DataStructure")
q.enquene("DataBase")
print(q.size, q.front.data, q.rear.data)
