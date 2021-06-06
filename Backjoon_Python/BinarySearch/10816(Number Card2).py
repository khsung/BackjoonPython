#10816 숫자 카드2 수정중
import sys
n=int(input())
n_arr=list(map(int,sys.stdin.readline().split()))
m=int(input())
m_arr=list(map(int,sys.stdin.readline().split()))
n_arr.sort()
n_arr_dic={}
n_arr_index=0
while n_arr_index<len(n_arr):
    cnt=0
    for i in range(n_arr_index,len(n_arr)):
        if i==n_arr_index:
            cnt+=1
        elif n_arr[i]!=n_arr[i-1]:
            n_arr_index=i
            n_arr_dic[n_arr[i-1]]=cnt
            break
        elif i==len(n_arr)-1:
            n_arr_index=i+1
            n_arr_dic[n_arr[i-1]]=cnt+1
            break
        else:
            cnt+=1
for i in range(len(m_arr)):
    if m_arr[i] in n_arr_dic:
        print(n_arr_dic[m_arr[i]],end=" ")
    else:
        print(0,end=" ")