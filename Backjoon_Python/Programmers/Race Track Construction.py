#경주로 건설
from collections import deque
import copy
def solution(board):
    answer = 100000
    board_cost=[[100000 for i in range(len(board[0]))] for j in range(len(board))]
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    queue=deque()
    if board[0][1]==0:
        queue.append([[[0,0],[0,1]],100,0])
        board_cost[0][1]=100
    if board[1][0]==0:
        queue.append([[[0,0],[1,0]],100,0])
        board_cost[1][0]=100
    while len(queue)>0:
        path,cost,cnt=queue.popleft()
        for i in dir:
            x=path[len(path)-1][0]+i[0]
            y=path[len(path)-1][1]+i[1]
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]==0 and [x,y] not in path:
                #직선일때
                if i[0]==path[len(path)-1][0]-path[len(path)-2][0] and i[1]==path[len(path)-1][1]-path[len(path)-2][1]:
                    if x==len(board)-1 and y==len(board[0])-1:
                        if answer>cost+100:
                            answer=cost+100
                    else:
                        if answer>cost+100 and board_cost[x][y]>=cost+100:
                            board_cost[x][y]=cost+100
                            temp_path=copy.deepcopy(path)
                            temp_path.append([x,y])
                            queue.append([temp_path,cost+100,cnt])
                        elif answer>cost+100 and cnt<1:
                            board_cost[x][y]=cost+100
                            temp_path=copy.deepcopy(path)
                            temp_path.append([x,y])
                            queue.append([temp_path,cost+100,cnt+1])
                else:
                    if x==len(board)-1 and y==len(board[0])-1:
                        if answer>cost+600:
                            answer=cost+600
                    else:
                        if answer>cost+600 and board_cost[x][y]>=cost+600:
                            board_cost[x][y]=cost+600
                            temp_path=copy.deepcopy(path)
                            temp_path.append([x,y])
                            queue.append([temp_path,cost+600,cnt])
                        elif answer>cost+100 and cnt<1:
                            board_cost[x][y]=cost+600
                            temp_path=copy.deepcopy(path)
                            temp_path.append([x,y])
                            queue.append([temp_path,cost+600,cnt+1])

    return answer
board=[[[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[0, 1, 1, 0, 0]]]
#board=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]
for i in range(len(board)):
    print(solution(board[i]))