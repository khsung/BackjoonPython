#10816 숫자 카드2
import sys
n=int(input())
first_array=list(map(int,sys.stdin.readline().split()))
first_array.sort()
m=int(input())
second_array=list(map(int,sys.stdin.readline().split()))
for i in second_array:
    left=0
    right=n-1
    cnt=0
    while left<=right:
        mid=(left+right)//2
        if first_array[mid]==i:
            cnt=first_array[left:right+1].count(i)
            break
        elif first_array[mid]<i:
            left=mid+1
        else:
            right=mid-1
    print(cnt,end=" ")