#15654 N과 M (5)
n,m=map(int,input().split())
visited=[0 for i in range(n)]
res_list=[]
def back_track(num_list,res_list):
    global visited
    if len(res_list)==m:
        for i in range(m):
            print(res_list[i], end=" ")
        print()
    else:
        for i in range(len(num_list)):
            if visited[i]==0:
                visited[i]=1
                res_list.append(num_list[i])
                back_track(num_list,res_list)
                res_list.pop()
                visited[i]=0

num_list=list(map(int,input().split()))
num_list.sort()
for i in range(n):
    visited[i]=1
    res_list.append(num_list[i])
    back_track(num_list,res_list)
    res_list.pop()
    visited[i]=0