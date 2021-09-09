#블록 이동하기
from collections import deque
def solution(board):
    answer=0
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    queue=deque()
    queue.append([[[0,0],[0,1]],0])
    robot={}
    while len(queue)>0 and answer==0:
        curr,cnt=queue.popleft()
        robot["".join(map(str,curr[0]))+"".join(map(str,curr[1]))]=1
        robot["".join(map(str,curr[1]))+"".join(map(str,curr[0]))]=1
        for i in range(len(curr)):
            for j in dir:
                x=curr[i][0]+j[0]
                y=curr[i][1]+j[1]
                if 0<=x<len(board) and 0<=y<len(board[0]) and [x,y]!=curr[(i+1)%2] and board[x][y]==0:
                    #print(curr,[x,y])
                    #가로일때
                    if curr[i][0]==curr[(i+1)%2][0]:
                        #옆으로 이동
                        if j[0]==0:
                            if x==len(board)-1 and y==len(board[0])-1:
                                answer=cnt+1
                            else:
                                if "".join(map(str,curr[i]))+"".join(map(str,[x,y])) not in robot:
                                    queue.append([[curr[i],[x,y]],cnt+1])
                        #세로로 이동
                        else:
                            if x==len(board)-1 and y==len(board[0])-1:
                                answer=cnt+1
                            else:
                                if board[x][curr[(i+1)%2][1]]==0 and "".join(map(str,curr[i]))+"".join(map(str,[x,y])) not in robot:
                                    queue.append([[curr[i],[x,y]],cnt+1])
                    #세로일때
                    else:
                        #세로로 이동
                        if j[1]==0:
                            if x==len(board)-1 and y==len(board[0])-1:
                                answer=cnt+1
                            else:
                                if "".join(map(str,curr[i]))+"".join(map(str,[x,y])) not in robot:
                                    queue.append([[curr[i],[x,y]],cnt+1])
                        #옆으로 이동
                        else:
                            if x==len(board)-1 and y==len(board[0])-1:
                                answer=cnt+1
                            else:
                                if board[curr[(i+1)%2][0]][y]==0 and "".join(map(str,curr[i]))+"".join(map(str,[x,y])) not in robot:
                                    queue.append([[curr[i],[x,y]],cnt+1])

    #print(robot)

    return answer

#board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
board=[[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(solution(board))