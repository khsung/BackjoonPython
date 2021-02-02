#10816 숫자 카드2
import sys
sys.setrecursionlimit(10**6)
def binary(array1,number,left,right):
    mid=(left+right)//2
    if array1[mid]==number:
        return array1.count(number)
    elif left==right:
        return 0
    else:
        if array1[mid]>number:
            return binary(array1,number,left,mid-1)
        else:
            return binary(array1,number,mid+1,right)

num1=int(input())
array1=list(map(int,input().split()))
num2=int(input())
array2=list(map(int,input().split()))
array1.sort()
for i in range(len(array2)):
    print(binary(array1,array2[i],0,len(array1)),end=" ")
