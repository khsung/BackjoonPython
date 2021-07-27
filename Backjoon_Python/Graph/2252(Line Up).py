#2252 줄 세우기
import sys
n,m=map(int,input().split())
parent=[i for i in range(n)]
visited=[0 for i in range(n)]

def find(a):
    global parent
    if a==parent[a]:
        return a
    else:
        return find(parent[a])

def union(a,b):
    pa=find(a)
    pb=find(b)
    parent[pb]=pa
    return parent[pb]

for i in range(m):
    temp=list(map(int,input().split()))
    union(temp[0]-1,temp[1]-1)
print(parent)