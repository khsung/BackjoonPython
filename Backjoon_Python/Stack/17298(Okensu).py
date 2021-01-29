#17298 Okensu  미완성
stack=[]
tempstack=[]
max=0
num=int(input())
res=[]
a=input()
stack=a.split(" ")
for i in range(num):
    if int(stack[-1])>max:
        res.append(-1)
        #print("-1",end=" ")
        max=int(stack[-1])
        stack.pop()
        tempstack.append(max)
    else:
        for j in reversed(range(len(tempstack))):
            if tempstack[j]>int(stack[-1]):
                #print(tempstack[j],end=" ")
                res.append(tempstack[j])
                tempstack.append(int(stack.pop()))
                break
res.reverse()
for i in range(len(res)):
    print(res[i],end=" ")