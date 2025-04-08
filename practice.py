#STACK -> LinkedList

class Node:     #스택 내부 링크드 리스트의 노드를 나타내는 클래스 정의
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None #top으로 사용할 instance 변수 정의

    def push(self, data):   #새 노드를 만듦
        node = Node(data)
        if self.top is None: #링크드리스트에 top이 없으면
            self.top = node #새 노드를 생성
        else:   #top이 있으면
            node.next = self.top #새 노드의 다음 요소에 기존 탑의 값을 할당
            self.top = node #새 노드를 탑으로 만듦

    def pop(self):
        if self.top is None: #스택이 비어 있을때 팝을 시도하면 예외를 일으킴
            raise IndexError('스택이 비었음.')
        poppednode = self.top.next #스택에 요소가 있을때는 링크드리스트의 첫번째 요소를 제거
        return poppednode.data #이를 반환
