class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self, **kwargs):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = None(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)