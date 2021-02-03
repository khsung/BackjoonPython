#9375 패션왕 신해빈
num=int(input())
result=[]
for i in range(num):
    res=[]
    num1=int(input())
    if num1==0:
        result.append(0)
    else:
        fashion=[]
        for j in range(num1):
            a,b=input().split()
            fashion.append(b)
        while len(fashion)!=0:
            tempcount=fashion.count(fashion[0])
            temp=fashion[0]
            res.append(tempcount+1)
            for k in range(tempcount):
                fashion.remove(temp)
        temp1=1
        for j in range(len(res)):
            temp1*=res[j]
        result.append(temp1-1)
for i in range(len(result)):
    print(result[i])
