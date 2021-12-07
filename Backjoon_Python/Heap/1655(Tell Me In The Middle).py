#1655 가운데를 말해요
import heapq
import sys

left_list=[]        #최대 힙
right_list=[]       #최소 힙
n=int(sys.stdin.readline())

for i in range(1,n+1):
    if i==1:
        left=int(sys.stdin.readline())
        print(left)
        heapq.heappush(left_list,(-left,left))
    elif i==2:
        right=int(sys.stdin.readline())
        if left>right:
            left,right=right,left
            heapq.heappop(left_list)
            heapq.heappush(left_list,(-left,left))
        print(left)
        heapq.heappush(right_list,right)
    else:
        mid=int(sys.stdin.readline())
        left=heapq.heappop(left_list)[1]
        right=heapq.heappop(right_list)

        #숫자 3개 정렬
        three_num=[left,mid,right]
        three_num.sort()
        left=three_num[0]
        mid=three_num[1]
        right=three_num[2]
        if i%2==0:
            heapq.heappush(left_list,(-left,left))
            heapq.heappush(right_list,mid)
            heapq.heappush(right_list,right)
            print(left_list[0][1])
        else:
            heapq.heappush(left_list,(-left,left))
            heapq.heappush(left_list,(-mid,mid))
            heapq.heappush(right_list,right)
            print(left_list[0][1])