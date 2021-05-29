#10816 숫자 카드2
n=int(input())
n_arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))
n_arr_set=list(set(n_arr))
n_arr_dic={}
for i in range(len(n_arr_set)):
    n_arr_dic[n_arr_set[i]]=n_arr.count(n_arr_set[i])
for i in m_arr:
    if i in n_arr_dic:
        print(n_arr_dic[i],end=" ")
    else:
        print(0,end=" ")