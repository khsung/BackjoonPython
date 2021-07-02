#1764 듣보잡
n,m=map(int,input().split())
dic={}
res=[]
for i in range(n):
    dic[input()]=1
for i in range(m):
    temp=input()
    if temp in dic:
        res.append(temp)
res.sort()
print(len(res))
for i in res:
    print(i)