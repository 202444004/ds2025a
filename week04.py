from re import search


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

    def remove(self, target):
        if self.head == target:
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if self.head.data == target:
                previous.link = current.link
            previous = current
            current = current.link

    #def is_find(self, target):
    def search(self, target):
        current = self.head
        while current.link:
            if target == current.link:
                return f"{target}을 찾았습니다."
            else:
                current = current.link
        return f"{target}은 리스트 안에 존재하지 않습니다."

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
#ll.remove(8)
print(ll)