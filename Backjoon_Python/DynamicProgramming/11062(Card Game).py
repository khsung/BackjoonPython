#11062 카드 게임
from collections import deque
testcase=int(input())
queue=deque()
for i in range(testcase):
    cnt=1
    res=0
    n=int(input())
    queue=deque(map(int,input().split()))
    while len(queue)>0:
        if queue[0]<queue[len(queue)-1]:
            temp=queue.pop()
        else:
            temp=queue.popleft()
        if cnt%2==1:
            res+=temp
        cnt+=1
    print(res)