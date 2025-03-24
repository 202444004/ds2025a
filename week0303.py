def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    #return list(s1.difference(s2))    #intersection 교집합 union 합집합 difference 차집합
    return list(s1 & s2)    #교집합
    #return list(s1 | s2)   #합집합
    #return list(s1 - s2)   #차집합

l1 = [45, 5, 22, 31, 7, 19]
l2 = [22, 1, 5, 2, 7, 28, 27, 19, 13, 41]

print(inters(l1, l2))

