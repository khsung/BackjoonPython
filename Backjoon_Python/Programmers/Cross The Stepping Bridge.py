#징검다리 건너기
import heapq
def solution(stones, k):
    visited=[0 for i in range(len(stones))]
    heap=[]
    for i in range(len(stones)):
        heapq.heappush(heap,[stones[i],i])
    cnt=0
    while True:
        temp=heapq.heappop(heap)
        answer=temp[0]
        cnt+=1
        visited[temp[1]]=1
        if cnt>=k:
            tempcnt=1
            tempright=templeft=temp[1]
            while tempright+1<len(visited):
                if visited[tempright+1]==1:
                    tempright+=1
                    tempcnt+=1
                else:
                    break
            while templeft-1>=0:
                if visited[templeft-1]==1:
                    templeft-=1
                    tempcnt+=1
                else:
                    break
            if tempcnt>=k:
                break
    return answer

stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k=3
print(solution(stones, k))