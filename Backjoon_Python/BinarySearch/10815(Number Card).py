#10815 숫자 카드
n=int(input())
n_arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))
n_arr.sort()
for i in range(len(m_arr)):
    left=0
    right=len(n_arr)-1
    check=False
    while left<=right:
        mid=(left+right)//2
        if n_arr[mid]==m_arr[i]:
            print(1,end=" ")
            check=True
            break
        elif n_arr[mid]<m_arr[i]:
            left=mid+1
        else:
            right=mid-1
    if not check:
        print(0,end=" ")