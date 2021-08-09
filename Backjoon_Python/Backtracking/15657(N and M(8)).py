#15657 N과 M (8)
n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()
curr_list=[]
def backtracking(curr_list,curr_index):
    global n_list,n,m
    if len(curr_list)==m:
        for i in curr_list:
            print(i,end=" ")
        print()
    else:
        for i in range(curr_index,n):
            curr_list.append(n_list[i])
            backtracking(curr_list,i)
            curr_list.pop()

for i in range(n):
    curr_list.append(n_list[i])
    backtracking(curr_list,i)
    curr_list.pop()