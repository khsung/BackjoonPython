#가장 먼 노드
def solution(n, edge):
    visited=[0 for i in range(n)]
    graph=[[]for i in range(n)]
    for i in range(len(edge)):
        graph[edge[i][0]-1].append(edge[i][1]-1)
        graph[edge[i][1]-1].append(edge[i][0]-1)

    answer=len(graph[0])
    queue=[]
    visited[0]=1
    curr_distance=1
    temp_cnt=0
    for i in range(len(graph[0])):
        queue.append([graph[0][i],curr_distance])
        visited[graph[0][i]]=1
    while len(queue)>0:
        temp=queue.pop(0)
        if temp[1]>curr_distance:
            temp_cnt=1
            curr_distance=temp[1]
        else:
            temp_cnt+=1
        for i in range(len(graph[temp[0]])):
            if visited[graph[temp[0]][i]]==0:
                visited[graph[temp[0]][i]]=1
                queue.append([graph[temp[0]][i],temp[1]+1])

    answer=temp_cnt
    return answer

n=6
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))