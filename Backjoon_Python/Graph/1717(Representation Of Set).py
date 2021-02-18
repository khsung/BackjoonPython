#1717 집합의 표현
n,m=map(int,input().split())
union_find=[i for i in range(n+1)]
for i in range(m):
    op,a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    if op==0:
        parenta=union_find[a]
        parentb=union_find[b]
        if parenta<parentb:
            while union_find.count(parentb)!=0:
                union_find[union_find.index(parentb)]=parenta
        elif parenta>parentb:
            parent=parentb
            while union_find.count(parentb)!=0:
                union_find[union_find.index(parenta)]=parentb
    else:
        while a!=union_find[a]:
            a=union_find[a]
        while b!=union_find[b]:
            b=union_find[b]
        if a==b:
            print("YES")
        else:
            print("NO")