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
def push_num(num):
    global heaps
    heaps.append(num)
    if len(heaps)>2:
        cur_index=len(heaps)-1
        while cur_index!=1:
            if heaps[cur_index]<heaps[cur_index//2]:
                heaps[cur_index],heaps[cur_index//2]=heaps[cur_index//2],heaps[cur_index]
                cur_index=cur_index//2
            else:
                break

def pop_num():
    global heaps
    if len(heaps)==1:
        print(0)
    else:
        print(heaps[1])
        heaps[1]=heaps[len(heaps)-1]
        heaps.pop()
        cur_index=1
        while True:
            #자식이 없을 때
            if len(heaps)<=cur_index*2:
                break
            #왼쪽자식만 있을 때
            elif len(heaps)<=cur_index*2+1:
                if heaps[cur_index]>heaps[cur_index*2]:
                    heaps[cur_index],heaps[cur_index*2]=heaps[cur_index*2],heaps[cur_index]
                else:
                    break
            else:
                if heaps[cur_index]<=heaps[2*cur_index] and heaps[cur_index]<=heaps[2*cur_index+1]:
                    break
                elif heaps[cur_index]>heaps[2*cur_index] and heaps[cur_index]<=heaps[2*cur_index+1]:
                    heaps[cur_index],heaps[cur_index*2]=heaps[cur_index*2],heaps[cur_index]
                    cur_index=cur_index*2
                elif heaps[cur_index]<=heaps[2*cur_index] and heaps[cur_index]>heaps[2*cur_index+1]:
                    heaps[cur_index],heaps[cur_index*2+1]=heaps[cur_index*2+1],heaps[cur_index]
                    cur_index=cur_index*2+1
                else:
                    if heaps[2*cur_index]<heaps[2*cur_index+1]:
                        heaps[cur_index],heaps[cur_index*2]=heaps[cur_index*2],heaps[cur_index]
                        cur_index=cur_index*2
                    else:
                        heaps[cur_index],heaps[cur_index*2+1]=heaps[cur_index*2+1],heaps[cur_index]
                        cur_index=cur_index*2+1

n=int(input())
heaps=[0]
for i in range(n):
    temp=int(sys.stdin.readline())
    if temp!=0:
        push_num(temp)
    else:
        pop_num()