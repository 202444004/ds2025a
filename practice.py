#STACK

class Stack:
    def __init__(self):
        self.items = [] #instance 변수 items 정의, 리스트 초기화

    def push(self, data):
        self.items.append(data) #append -> items에 새로운 데이터 추가

    def pop(self):
        return self.items.pop() #pop -> 가장 최근 추가된 요소(top) 반환 -> 삭제

    def size(self):
        return len(self.items) #len -> 스택의 길이 반환

    def is_empty(self):
        return len(self.items) == 0 #len == 0 이면 리스트가 비어있음

    def peek(self):
        return self.items[-1] #스택의 가장 마지막, 최근 추가된 요소(top) 반환