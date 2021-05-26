#18870 좌표 압축
num=int(input())
arr=list(map(int,input().split()))
set_arr=set(arr)
set_arr=list(set_arr)
set_arr.sort()
for i in range(num):
    print(set_arr.index(arr[i]),end=" ")