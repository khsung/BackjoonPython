#10816 숫자 카드2
num1=int(input())
array1=list(map(int,input().split()))
num2=int(input())
array2=list(map(int,input().split()))
for i in range(len(array2)):
    print(array1.count(array2[i]),end=" ")
