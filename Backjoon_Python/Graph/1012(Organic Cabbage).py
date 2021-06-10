#1012 유기농배추
testcase=int(input())
for i in range(testcase):
    queue=[]
    res=0
    M,N,K=map(int,input().split())
    graph=[[0 for j in range(M)]for k in range(N)]
    for j in range(K):
        tempm,tempn=map(int,input().split())
        graph[tempn][tempm]=1
    for j in range(N):
        for k in range(M):
            if graph[j][k]==1:
                res+=1
                queue.append([j,k])
                graph[j][k]=0
                while len(queue)>0:
                    tempn,tempm=queue.pop()
                    if tempn-1>=0 and graph[tempn-1][tempm]==1:
                        graph[tempn-1][tempm]=0
                        queue.append([tempn-1,tempm])
                    if tempn+1<N and graph[tempn+1][tempm]==1:
                        graph[tempn+1][tempm]=0
                        queue.append([tempn+1,tempm])
                    if tempm-1>=0 and graph[tempn][tempm-1]==1:
                        graph[tempn][tempm-1]=0
                        queue.append([tempn,tempm-1])
                    if tempm+1<M and graph[tempn][tempm+1]==1:
                        graph[tempn][tempm+1]=0
                        queue.append([tempn,tempm+1])
    print(res)