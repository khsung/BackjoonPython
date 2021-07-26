#1717 집합의 표현
import sys
sys.setrecursionlimit(10**9)
n,m=map(int,sys.stdin.readline().split())
union_find=[i for i in range(n+1)]
print(union_find)
def find(a):
    global union_find
    if union_find[a]==a:
        return a
    else:
        union_find[a]=find(union_find[a])
        return union_find[a]

for i in range(m):
    temp=list(map(int,sys.stdin.readline().split()))
    if temp[0]==0:
        if temp[1]<temp[2]:
            temp[1],temp[2]=temp[2],temp[1]
        union_find[temp[1]]=temp[2]
    else:
        if find(temp[1])==find(temp[2]):
            print("YES")
        else:
            print("NO")
    print(union_find)