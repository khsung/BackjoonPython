#15657 N과 M (8)
n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()
check_list=[]
def back_tracking(curr_list):
    global n,m,n_list
    global check_list
    print("curr_list,check_list=",curr_list,check_list)
    if len(curr_list)==m:
        if curr_list not in check_list:
            check_list.append(curr_list)
            for i in curr_list:
                print(i,end=" ")
            print()
    else:
        for i in range(n):
            curr_list.append(n_list[i])
            back_tracking(curr_list)
            curr_list.pop()
for i in range(n):
    back_tracking([n_list[i]])
#print(check_list)