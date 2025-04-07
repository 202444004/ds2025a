def is_valid_parenthese(expression : str) -> bool: # type hint str-> parameter data , bool-> type
    stack = list()
    brackets = {']':'[', '}':'{', ')':'('}
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack

#def check(exprs : str) -> bool:
    #brackets = {'}':'{',')':'('}
    #for brackets in exprs:
        #if brackets.keys()== "}":

print(is_valid_parenthese("[({1+2)]}"))
print(is_valid_parenthese("[({1+2})]"))
print(is_valid_parenthese(")1+2()"))
print(is_valid_parenthese("(1+2))"))
print(is_valid_parenthese("(1+2)"))
print(is_valid_parenthese("((3*2)/2)"))