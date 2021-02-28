#2309 일곱 난쟁이
array=[]
sum=0
for i in range(9):
    num=int(input())
    array.append(num)
    sum+=num
sum-=100
for i in range(8):
    for j in range(i+1,9):
        if array[i]+array[j]==sum:
            tempi=array[i]
            tempj=array[j]
array.remove(tempi)
array.remove(tempj)
array.sort()
for i in array:
    print(i)