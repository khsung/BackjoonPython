#14620 꽃길
N=int(input())
graph=[]
flowers=[]
dir=[[0,0],[1,0],[-1,0],[0,1],[0,-1]]
min_sum=4000
for i in range(N):
    temp=list(map(int,input().split()))
    graph.append(temp)
for i in range(1,N-1):          #첫번째 꽃
    for j in range(1,N-1):
        flowers.append([i,j])
        for k in range(1,N-1):          #두번째 꽃
            for l in range(1,N-1):
                if abs(flowers[0][0]-k)+abs(flowers[0][1]-l)>=3:
                    flowers.append([k,l])
                    for m in range(1,N-1):          #세번째 꽃
                        for n in range(1,N-1):
                            if abs(flowers[0][0]-m)+abs(flowers[0][1]-n)>=3 and abs(flowers[1][0]-m)+abs(flowers[1][1]-n)>=3:
                                sum=0
                                flowers.append([m,n])
                                for x in flowers:
                                    for y in dir:
                                        sum+=graph[x[0]+y[0]][x[1]+y[1]]
                                if min_sum>sum:
                                    min_sum=sum
                                flowers.pop()
                if len(flowers)>1:
                    flowers.pop()
        flowers.pop()
print(min_sum)