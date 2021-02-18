#11725 트리의 부모 찾기
n=int(input())
save_path=[]
tree_parent=[0 for i in range(n+1)]
for i in range(n-1):
    a,b=map(int, input().split())
    if a==1:
        tree_parent[b]=a
    elif b==1:
        tree_parent[a]=b
    elif tree_parent[a]==0 and tree_parent[b]==0:
        save_path.append([a,b])
    else:
        if tree_parent[a]==0:
            tree_parent[a]=b
        elif tree_parent[b]==0:
            tree_parent[b]=a
        #else:
        #    print("=")

while len(save_path)>0:
    a=save_path[0][0]
    b=save_path[0][1]
    if tree_parent[a]==0:
        tree_parent[a]=b
        save_path.pop(0)
    elif tree_parent[b]==0:
        tree_parent[b]=a
        save_path.pop(0)
    else:
        save_path.pop(0)
        save_path.append([a,b])
    
for i in range(2,n+1):
    print(tree_parent[i])