#11438 LCA2
import sys
sys.setrecursionlimit(10**8)
n=int(input())
parent=[i for i in range(n)]

def find_p(a):
    global parent
    if a==parent[a]:
        return a
    else:
        return find_p(parent[a])

def find_com_p(a,b):
    global parent
    if a==parent[b]:
        print(a+1)
    elif b==parent[a]:
        print(b+1)
    elif parent[a]==parent[b]:
        print(parent[a]+1)
    else:
        if parent[a]<parent[b]:
            return find_com_p(a,parent[b])
        else:
            return find_com_p(parent[a],b)

def union(a,b):
    global parent
    pa=find_p(a)
    pb=find_p(b)
    parent[pb]=pa
    return parent[pb]

tree_info=[]

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    tree_info.append([a,b])
tree_info.sort(key=lambda x:(x[0],x[1]))
for i in tree_info:
    if 1 in i:
        if i[1]<i[0]:
            i[0],i[1]=i[1],i[0]
        union(i[0]-1,i[1]-1)
    else:
        if find_p(i[0]-1)>find_p(i[1]-1):
            parent[i[0]-1]=i[1]-1
        else:
            parent[i[1]-1]=i[0]-1

m=int(input())
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    find_com_p(a-1,b-1)