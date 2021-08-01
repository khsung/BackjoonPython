#9019 DSLR
from collections import deque
import sys
test_case=int(input())
for i in range(test_case):
    visited=[0 for i in range(10000)]
    queue=deque()
    numbers=list(map(int,sys.stdin.readline().split()))
    queue.append([numbers[0],""])
    while len(queue)>0:
        temp=queue.popleft()

        temp_D=(temp[0]*2)%10000
        if temp_D==numbers[1]:
            print(temp[1]+"D")
            break
        elif visited[temp_D]==0:
            queue.append([temp_D,temp[1]+"D"])
            visited[temp_D]=1

        if temp[0]==0:
            temp_S=9999
        else:
            temp_S=temp[0]-1
        if temp_S==numbers[1]:
            print(temp[1]+"S")
            break
        elif visited[temp_S]==0:
            queue.append([temp_S,temp[1]+"S"])
            visited[temp_S]=1

        temp_L=10*(temp[0]%1000)+temp[0]//1000
        if temp_L==numbers[1]:
            print(temp[1]+"L")
            break
        elif visited[temp_L]==0:
            queue.append([temp_L,temp[1]+"L"])
            visited[temp_L]=1

        temp_R=temp[0]//10+(temp[0]%10)*1000
        if temp_R==numbers[1]:
            print(temp[1]+"R")
            break
        elif visited[temp_R]==0:
            queue.append([temp_R,temp[1]+"R"])
            visited[temp_R]=1