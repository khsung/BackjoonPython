#10816 숫자 카드2
import sys
n=int(input())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(input())
m_list=list(map(int,sys.stdin.readline().split()))
n_list.sort()
for i in range(m):
    left=0
    right=n-1
    target=-1
    while left<=right:
        mid=(left+right)//2
        if n_list[mid]==m_list[i]:
            target=mid
            break
        elif n_list[mid]<m_list[i]:
            left=mid+1
        else:
            right=mid-1
    if target==-1:
        print(0,end=" ")
    else:
        min_target=max_target=target
        left=0
        right=min_target
        while left<=right:
            mid=(left+right)//2
            if n_list[mid]==m_list[i]:
                if min_target>mid:
                    min_target=mid
                right=mid-1
            else:
                left=mid+1
        left=max_target
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if n_list[mid]==m_list[i]:
                if mid>max_target:
                    max_target=mid
                left=mid+1
            else:
                right=mid-1

        print(max_target-min_target+1,end=" ")