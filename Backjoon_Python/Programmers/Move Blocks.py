#블록 이동하기
from collections import deque
def solution(board):
    answer = 110000
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    visited=[[0 for i in range(len(board[0]))]for j in range(len(board))]
    visited[0][0]=1
    visited[0][1]=1

    queue=deque()
    queue.append([[[0,0],[0,1]],0])
    while len(queue)>0:
        curr,cnt=queue.popleft()
        for i in range(len(curr)):
            for j in range(len(dir)):
                x=curr[i][0]+dir[j][0]
                y=curr[i][1]+dir[j][1]
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]==0 and curr[(i+1)%2]!=[x,y] and visited[x][y]<10:
                    if board[curr[(i+1)%2][0]+dir[j][0]][curr[(i+1)%2][1]+dir[j][1]]==0:
                        if x==len(board)-1 and y==len(board[0])-1:
                            if answer>cnt+1:
                                answer=cnt+1
                        else:
                            queue.append([[curr[i],[x,y]],cnt+1])
                            visited[x][y]+=1
    return answer

board=[[0, 0, 0, 0, 0, 0, 1], 
       [1, 1, 1, 1, 0, 0, 1], 
       [0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 1, 1, 1, 1, 0], 
       [0, 1, 1, 1, 1, 1, 0], 
       [0, 0, 0, 0, 0, 1, 1], 
       [0, 0, 1, 0, 0, 0, 0]]
print(solution(board))