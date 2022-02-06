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
    changed_col=[]
    del_queue=[]
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
                            visited[dy][dx]=1

                if temp_cnt>=4:
                    check=False
                    changed_col.append(j)
                    del_queue.append([i,j])
                    while len(del_queue)>0:
                        temp=del_queue.pop(0)
                        graph[i][j]="."
                        for k in range(len(dir)):
                            dy=dir[k][0]+temp[0]
                            dx=dir[k][1]+temp[1]
                            if 0<=dy<12 and 0<=dx<6 and graph[dy][dx]==curr_char:
                                del_queue.append([dy,dx])
                                graph[dy][dx]="."
                                if dx not in changed_col:
                                    changed_col.append(dx)

    if check:
        break
    else:
        res+=1
        for i in range(len(changed_col)):
            for j in range(10,-1,-1):
                if graph[j][changed_col[i]]!=".":
                    curr=j
                    while curr<=10 and graph[curr+1][changed_col[i]]==".":
                        graph[curr+1][changed_col[i]],graph[curr][changed_col[i]]=graph[curr][changed_col[i]],graph[curr+1][changed_col[i]]
                        curr+=1

print(res)