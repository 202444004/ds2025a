class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            #raise IndexError("스택이 비었음")
            return "스택 비었음"

        popped_node = self.top #연결 설정 코드
        popped_node.link = None #^^
        self.top = self.top.link #^^
        return popped_node.data

s1 = Stack()
print(s1.pop())
s1.push("Data structure")
s1.push("Database")
print(s1.pop())
print(s1.pop())