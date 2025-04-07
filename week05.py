def is_valid_parenthese(expression : str) -> bool: # type hint str-> parameter data , bool-> type
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_valid_parenthese("(1+2))"))
print(is_valid_parenthese("(1+2)"))
print(is_valid_parenthese("((3*2)/2)"))