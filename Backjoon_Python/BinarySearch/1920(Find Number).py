#1920 수 찾기
num1=int(input())
array1=list(map(int,input().split()))
num2=int(input())
array2=list(map(int,input().split()))
for i in range(len(array2)):
    if array2[i] in array1:
        print("1")
    else:
        print("0")