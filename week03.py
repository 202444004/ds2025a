def myZip(l1, l2):
    l3 = list()
    length = 0
    if len(l1) < len(l2):
        length = len(l1)
    else:
        length = len(l2)

    for i in range(length):
        l3.append((l1[i], l2[i]))
    return l3

group = ['BlackPink', 'Hot', 'Seventeen', 'NJZ']
ratings = [1,2,4,3]
#ratings = [1,2,4,3,100]

group_rating = myZip(group,ratings)
print(group_rating)