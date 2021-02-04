#2997 4번째 수
a,b,c=input().split()
array=[]
array.append(int(a))
array.append(int(b))
array.append(int(c))
array.sort()
if array[1]-array[0] == array[2]-array[1]:
    print(2*array[2]-array[1])
else:
    if array[1]-array[0] < array[2]-array[1]:
        print(2*array[1]-array[0])
    else:
        print(2*array[1]-array[2])