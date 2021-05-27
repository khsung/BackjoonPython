#18870 좌표 압축
import sys
num=int(input())
arr=list(map(int,sys.stdin.readline().split()))
set_arr=list(set(arr))
set_arr.sort()
dic_arr={}
count=0
#딕셔너리를 이용한 시간 단축
for i in set_arr:
    dic_arr[i]=count
    count+=1
for i in range(num):
    print(dic_arr[arr[i]],end=" ")