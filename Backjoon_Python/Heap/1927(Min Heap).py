#1927 최소 힙
#import heapq
#import sys
#num=int(input())
#array=[]
#res=[]
#for i in range(num):
#    a=int(sys.stdin.readline())
#    if a==0:
#        if len(array)==0:
#            print(0)
#        else:
#            print(heapq.heappop(array))
#    else:
#        heapq.heappush(array, a) 

#연습
import sys
heap=[0]
n=int(input())
for i in range(n):
    temp=int(sys.stdin.readline())
    if temp==0:
        if len(heap)==1:
            print(0)
        else:
            print(heap[1])
            heap[1]=heap[len(heap)-1]
            heap.pop()
            curr_index=1
            while True:
                left=curr_index*2
                right=left+1
                if left>=len(heap):
                    break
                elif right>=len(heap):
                    if heap[curr_index]>heap[left]:
                        heap[curr_index],heap[left]=heap[left],heap[curr_index]
                        curr_index=left
                    else:
                        break
                else:
                    if heap[left]>=heap[curr_index] and heap[right]>=heap[curr_index]:
                        break
                    elif heap[left]<heap[curr_index] and heap[right]>heap[curr_index]:
                        heap[curr_index],heap[left]=heap[left],heap[curr_index]
                        curr_index=right
                    elif heap[right]<heap[curr_index] and heap[left]>heap[curr_index]:
                        heap[curr_index],heap[right]=heap[right],heap[curr_index]
                        curr_index=left
                    else:
                        if heap[right]>heap[left]:
                            heap[curr_index],heap[left]=heap[left],heap[curr_index]
                            curr_index=left
                        else:
                            heap[curr_index],heap[right]=heap[right],heap[curr_index]
                            curr_index=right
    else:
        heap.append(temp)
        curr_index=len(heap)-1
        while curr_index!=1:
            if heap[curr_index]<heap[curr_index//2]:
                heap[curr_index],heap[curr_index//2]=heap[curr_index//2],heap[curr_index]
                curr_index=curr_index//2
            else:
                break
    print(heap)