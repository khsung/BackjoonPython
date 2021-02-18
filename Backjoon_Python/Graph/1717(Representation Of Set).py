#1717 집합의 표현 미완성
n,m=int(input().split())
union_find=[i for i in range(n+1)]
for i in range(m):
    op,a,b=int(input().split())
    if a>b:
        a,b=b,a
    if op==0:

    else:
