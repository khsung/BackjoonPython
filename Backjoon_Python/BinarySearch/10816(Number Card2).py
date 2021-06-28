#10816 숫자 카드2
import sys
n=int(input())
first_array=list(map(int,sys.stdin.readline().split()))
first_array.sort()
m=int(input())
second_array=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    left=0
    right=n-1
    cnt=0
    check=True
    while left<=right and check==True:
        mid=(left+right)//2
        if first_array[mid]==second_array[i]:
            temp_dis=0
            while True:
                if mid>=0 and first_array[mid]==second_array[i]:
                    mid-=1
                    temp_dis+=1
                else:
                    temp_dis-=1
                    mid+=1
                    break
            mid+=temp_dis
            cnt+=temp_dis
            while mid<n and first_array[mid]==second_array[i]:
                cnt+=1
                mid+=1
            check=False
        elif first_array[mid]<second_array[i]:
            left=mid+1
        else:
            right=mid-1
    print(cnt,end=" ")
