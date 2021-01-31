#7568 Bulk
num=int(input())
array=[]
for i in range(num):
    a,b=input().split()
    array.append([a,b])
array.sort()
print(array)