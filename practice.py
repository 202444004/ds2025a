#Stack-Reverse
#1 #a_string[::-1]
#2 #''.join(reversed('a_string'))
#3  Stack 사용하기
def reverse_string(a_string):   #매개변수: 문자열
    stack = []  #
    string = ""
    for c in a_string:
        stack.append(c) #각 문자를 스택에 추가
    for c in a_string:
        string += stack.pop()   #각 문자를 a_string에 추가
    return string   #뒤집힌 문자열 반환

print(reverse_string("Biever"))