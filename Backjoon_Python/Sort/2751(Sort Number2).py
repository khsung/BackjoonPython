
#2751 Sort Number2
import heapq
num=int(input())
numbers=[]
for i in range(num):
    numbers.append(int(input()))
heap=[]
sorted_num=[]
for i in numbers:
    heapq.heappush(heap,i)
while heap:
    sorted_num.append(heapq.heappop(heap))
for i in range(len(sorted_num)):
    print(sorted_num[i])