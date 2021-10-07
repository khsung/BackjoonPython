#게임 맵 최단거리
from collections import deque
def solution(maps):
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    visited=[[0 for i in range(len(maps[0]))]for j in range(len(maps))]
    desx=len(maps)-1
    desy=len(maps[0])-1
    answer = -1
    path=deque()
    path.append([0,0,1])
    visited[0][0]=1
    while len(path)>0:
        x,y,cnt=path.popleft()
        for i in range(4):
            dx=x+dir[i][0]
            dy=y+dir[i][1]
            if dx==desx and dy==desy:
                answer=cnt+1
                path=deque()
                break
            elif 0<=dx<=desx and 0<=dy<=desy and maps[dx][dy]==1 and visited[dx][dy]==0:
                visited[dx][dy]=1
                path.append([dx,dy,cnt+1])
    return answer

maps=[[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
for i in range(len(maps)):
    print(solution(maps[i]))