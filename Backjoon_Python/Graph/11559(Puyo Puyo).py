#11559 Puyo Puyo
graph=[]
dir=[[-1,0],[1,0],[0,-1],[0,1]]
queue=[]
for i in range(12):
    graph.append(list(input()))
res=0

while True:
    check=True
    visited=[[0 for i in range(6)]for j in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j]!="." and visited[i][j]==0:
                curr_char=graph[i][j]
                temp_cnt=0
                queue.append([i,j])
                visited[i][j]=1
                while len(queue)>0:
                    curr=queue.pop(0)
                    temp_cnt+=1
                    for k in range(len(dir)):
                        dy=dir[k][0]+curr[0]
                        dx=dir[k][1]+curr[1]
                        if 0<=dy<12 and 0<=dx<6 and graph[dy][dx]==curr_char and visited[dy][dx]==0:
                            queue.append([dy,dx])

                if temp_cnt>=4:
                    check=False
                    #i,j 좌표부터 시작해서 .으로 치환

    if check:
        break


print(res)