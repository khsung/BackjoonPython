#이진탐색 구현
data=[1,2,4,5,6,8,9]

def binary(n):
    index=-1
    left=0
    right=len(data)-1
    while left<=right:
        mid=(left+right)//2
        if data[mid]==n:
            index=mid
            break
        elif n<data[mid]:
            right=mid-1
        else:
            left=mid+1
    return index

first=binary(2)

if first==-1:
    print("없는 원소입니다.")
else:
    print(first,"번째 인덱스에 있습니다.")

second=binary(7)

if second==-1:
    print("없는 원소입니다.")
else:
    print(second,"번째 인덱스에 있습니다.")