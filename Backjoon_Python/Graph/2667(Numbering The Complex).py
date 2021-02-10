#2667 단지번호붙이기
num=int(input())
visited=[[0 for i in range(num)]for j in range(num)]
graph=[]
counts=[]
for i in range(num):
    temp=[]
    tempstring=input()
    for j in range(len(tempstring)):
        temp.append(int(tempstring[j]))
    graph.append(temp)
def bfs(i,j,countsindex):
    global visited
    global graph
    global counts
    global num
    global cnt
    tempcnt=cnt
    visited[i][j]=1
    if i-1>=0 and visited[i-1][j]==0 and graph[i-1][j]==1:
        cnt+=1
        bfs(i-1,j,countsindex)
    if j+1<num and visited[i][j+1]==0 and graph[i][j+1]==1:
        cnt+=1
        bfs(i,j+1,countsindex)
    if i+1<num and visited[i+1][j]==0 and graph[i+1][j]==1:
        cnt+=1
        bfs(i+1,j,countsindex)
    if j-1>=0 and visited[i][j-1]==0 and graph[i][j-1]==1:
        cnt+=1
        bfs(i,j-1,countsindex)
    if tempcnt==cnt:
        counts[countsindex].append(tempcnt)
countsindex=-1
for i in range(num):
    for j in range(num):
        if visited[i][j]==0 and graph[i][j]==1:
            counts.append([])
            countsindex+=1
            cnt=1
            bfs(i,j,countsindex)
            counts[countsindex]=max(counts[countsindex])
counts.sort()
print(len(counts))
for i in range(len(counts)):
    print(counts[i])
