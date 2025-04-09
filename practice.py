#MinStack
class MinStack():
    def __init__(self):
        #instance 변수 정의
        self.main = []  #메인 스택
        self.min = []   #가장 작은 요소 추적

    def push(self, n):
        if len(self.main) == 0: #self.main이 비어 있는지 확인
            self.min.append(n) #self.main == 0 -> 어떤 값이 들어와도 가장 작은 값임. => min에 추가
        elif n <= self.min[-1]: #비어있지 않다면 n이 self.min의 마지막 요소보다 작거나 같은지 비교
            self.min.append(n)  #작거나 같으면 n이 가장 작은 값임. => min에 추가
        else:   #n이 클경우
            self.min.append(self.min[-1]) #self.min의 마지막 요소가 여전히 가장 작은 값. => 다시 추가
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]

min_stack =MinStack()
min_stack.push(10)
print(min_stack.main)
print(min_stack.min)

min_stack.push (15)
print(min_stack.main)   #main -> 요소를 추가한 순서대로 저장하는 일반적인 스택
print(min_stack.min)    #min -> 스택에 추가된 순서를 유지하지 않고 가장 작은 숫자만 추적

print(min_stack.get_min())

min_stack.pop()
print(min_stack.main)
print(min_stack.min)

print(min_stack.get_min())

min_stack.pop()
print(min_stack.main)
print(min_stack.min)
