#2484 주사위 네개
n=int(input())
max=0
for i in range(n):
    score=list(map(int,input().split()))
    temp=[0 for j in range(6)]
    for j in range(4):
        temp[score[j]-1]+=1
    if 4 in temp:
        temp_max=5000*(temp.index(4)+1)+50000
    elif 3 in temp:
        temp_max=1000*(temp.index(3)+1)+10000
    elif 2 in temp:
        if temp.count(2)==1:
            temp_max=100*(temp.index(2)+1)+1000
        else:
            temp_max=500*(temp.index(2)+1)+2000
            temp[temp.index(2)]=0
            temp_max+=500*(temp.index(2)+1)
    else:
        temp[temp.index(1)]=0
        temp[temp.index(1)]=0
        temp[temp.index(1)]=0
        temp_max=100*(temp.index(1)+1)
    if max<temp_max:
        max=temp_max
print(max)