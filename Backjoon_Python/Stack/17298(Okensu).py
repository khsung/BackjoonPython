#17298 오큰수
import sys
templist=[]
res_array=[]
num=int(input())
stack_array=list(map(int, sys.stdin.readline().split()))
while len(stack_array)>0:
    temp=stack_array.pop()
    check=0
    for i in range(len(templist)):
        if templist[i]>temp:
            res_array.insert(0,templist[i])
            check=1
            break
    if check==0:
        res_array.insert(0,-1)
    templist.insert(0,temp)
print(res_array)
