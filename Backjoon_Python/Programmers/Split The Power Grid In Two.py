#전력망을 둘로 나누기
from collections import deque
def solution(n, wires):
    answer = n
    tree=[[] for i in range(n)]
    for i in range(len(wires)):
        tree[wires[i][0]-1].append(wires[i][1]-1)
        tree[wires[i][1]-1].append(wires[i][0]-1)
    for i in range(len(wires)):
        tree[wires[i][0]-1].remove(wires[i][1]-1)
        tree[wires[i][1]-1].remove(wires[i][0]-1)
        queue=deque()
        queue.append(0)
        temp_sum=1
        visited=[0 for j in range(n)]
        visited[0]=1
        while len(queue)>0:
            curr=queue.popleft()
            for j in range(len(tree[curr])):
                if visited[tree[curr][j]]==0:
                    visited[tree[curr][j]]=1
                    queue.append(tree[curr][j])
                    temp_sum+=1
        if abs(n-temp_sum*2)<answer:
            answer=abs(n-temp_sum*2)
        tree[wires[i][0]-1].append(wires[i][1]-1)
        tree[wires[i][1]-1].append(wires[i][0]-1)

    return answer

n=[9,4,7]
wires=[[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],[[1,2],[2,3],[3,4]],[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]
for i in range(len(wires)):
    print(solution(n[i], wires[i]))