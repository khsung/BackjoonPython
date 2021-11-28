#D번 - 버스 노선 개편하기
n=int(input())
bus=[]
res=[]
for i in range(n):
    bus.append(list(map(int,input().split())))
bus.sort(key=lambda x:(x[0],x[1]))
check=True
for i in bus:
    if check:
        res.append(i)
        check=False
    else:
        if i[0]<=res[len(res)-1][1]:
            if i[1]>res[len(res)-1][1]:
                res[len(res)-1][1]=i[1]
            if res[len(res)-1][2]>i[2]:
                res[len(res)-1][2]=i[2]
        else:
            res.append(i)
print(len(res))
for i in res:
    print(i[0],i[1],i[2])