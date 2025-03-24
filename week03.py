#l = [99, 0, -7, 0, 16]

#for i in range(len(l)):
    #print(f"{l[i]}, {id(l[i])}")

import array

arr = array.array('f', [99, 0, -7, 0, 16])
for i in range(len(arr)):
    print(f"{arr[i]:3}, {id(arr[i])}")