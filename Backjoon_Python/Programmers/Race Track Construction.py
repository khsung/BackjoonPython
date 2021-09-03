#경주로 건설
from collections import deque
import copy
def solution(board):
    answer = 100000
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    queue=deque()
    queue.append([[[0,0]],0])
    while len(queue)>0:
        print(queue)
        temp=queue.popleft()
        for i in range(4):
            print(temp[0][len(temp[0])-1][0])
            x=temp[0][len(temp[0])-1][0]+dir[i][0]
            y=temp[0][len(temp[0])-1][1]+dir[i][1]
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]==0:
                if len(temp[0])==1:
                    temp=copy.deepcopy(temp[0])
                    temp.append([x,y])
                    queue.append([temp,100])
                else:
                    if [x,y] not in temp[0]:
                        temp_cost=temp[1]
                        #print(temp[0][len(temp[0])-1][0]-temp[0][len(temp[0])-2][0],x-temp[0][len(temp[0])-1][0],temp[0][len(temp[0])-1][1]-temp[0][len(temp[0])-2][1],y-temp[0][len(temp[0])-1][1])
                        if (temp[0][len(temp[0])-1][0]-temp[0][len(temp[0])-2][0])==(x-temp[0][len(temp[0])-1][0]) and (temp[0][len(temp[0])-1][1]-temp[0][len(temp[0])-2][1])==(y-temp[0][len(temp[0])-1][1]):
                            #print(temp[0][len(temp[0])-1],temp[0][len(temp[0])-2],x,y)
                            #print(temp[0][len(temp[0])-1][0]-temp[0][len(temp[0])-2][0],x-temp[0][len(temp[0])-1][0],temp[0][len(temp[0])-1][1]-temp[0][len(temp[0])-2][1],y-temp[0][len(temp[0])-1][1])
                            temp_cost+=100
                        else:
                            temp_cost+=500
                        if x==len(board)-1 and y==len(board[0])-1:
                            if answer>temp_cost:
                                answer=temp_cost
                                temp=copy.deepcopy(temp[0])
                                temp.append([x,y])
                                print(temp)
                        else:
                            temp=copy.deepcopy(temp[0])
                            temp.append([x,y])
                            queue.append([temp,temp_cost])
    return answer

board=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]
for i in range(len(board)):
    print(solution(board[i]))