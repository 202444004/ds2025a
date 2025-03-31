class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self, **kwargs):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} + -> "
            current = current.link
        return result + "END"
        #return "Linked List"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)