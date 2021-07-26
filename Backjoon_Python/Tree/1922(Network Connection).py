#1922 네트워크 연결
n=int(input())
m=int(input())
cost=[]
cnt=0
parent=[i for i in range(n+1)]
res=0
def find_p(a):
    global parent
    if a==parent[a]:
        return a
    else:
        parent[a]=find_p(parent[a])
        return parent[a]

def union(a,b):
    pa=find_p(a)
    pb=find_p(b)
    if pa<pb:
        pa,pb=pb,pa
    parent[pa]=pb
    return parent[pa]

for i in range(m):
    temp=list(map(int,input().split()))
    cost.append(temp)
cost.sort(key=lambda x:x[2])

for i in cost:
    if find_p(i[0])!=find_p(i[1]):
        cnt+=1
        res+=i[2]
        union(i[0],i[1])
    if cnt==n-1:
        break
print(res)