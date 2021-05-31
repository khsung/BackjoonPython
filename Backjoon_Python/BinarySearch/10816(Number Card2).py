#10816 숫자 카드2 수정중
n=int(input())
n_arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))
n_arr_set=list(set(n_arr))
n_arr.sort()
n_arr_dic={}
n_arr_index=0
n_arr_set_index=0
print(n_arr)
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
        else:
            cnt+=1
    print("n_arr_index=",n_arr_index)
    print("cnt=",cnt)
print(n_arr_dic)