#1012 유기농배추 구현중
testcase=int(input())
queue=[]
for i in range(testcase):
    m,n,k=input().split()
    m=int(m)
    n=int(n)
    k=int(k)
    cnt=0
    graph=[[0 for a in range(m)]for b in range(n)]
    for j in range(k):
        target=list(map(int,input().split()))
        graph[target[1]][target[0]]=1
        for y in range(n):
            for x in range(m):
                if graph[y][x]==1:
                    queue.append([y,x])
                    while len(queue)>0:
                        tempy,tempx=queue.pop(0)
                        graph[tempy][tempx]=0
                        if tempx-1>=0 and graph[tempy][tempx-1]==1:
                            queue.append([tempy,tempx-1])
    print(cnt)
    #for j in range(k):
    #    target=list(map(int,input().split()))
    #    graph[target[1]][target[0]]=1
    #    for y in range(n):
    #        for x in range(m):
    #            if graph[y][x]==1:
    #                queue.append([y,x])
    #                while len(queue)>0:
    #                    tempy,tempx=queue.pop(0)
    #                    graph[tempy][tempx]=0
    #                    if tempx-1>=0 and graph[tempy][tempx-1]==1:
    #                        queue.append([tempy,tempx-1])
    #print(cnt)