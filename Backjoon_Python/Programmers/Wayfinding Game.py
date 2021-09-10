#길 찾기 게임
import sys
sys.setrecursionlimit(10**6)
def pre(tree,curr):
    global answer
    answer[0].append(curr)
    if tree[curr][1]!=".":
        pre(tree,tree[curr][1])
    if tree[curr][2]!=".":
        pre(tree,tree[curr][2])

def post(tree,curr):
    global answer
    if tree[curr][1]!=".":
        post(tree,tree[curr][1])
    if tree[curr][2]!=".":
        post(tree,tree[curr][2])
    answer[1].append(curr)

def solution(nodeinfo):
    global answer
    answer = [[],[]]
    tree={}
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:(-x[1]))
    root=nodeinfo[0][2]
                #x좌표, left, right
    tree[root]=[nodeinfo[0][0],".","."]
    for i in range(1,len(nodeinfo)):
        curr=root
        while True:
            #left
            if tree[curr][0]>nodeinfo[i][0]:
                if tree[curr][1]==".":
                    tree[curr][1]=nodeinfo[i][2]
                    tree[nodeinfo[i][2]]=[nodeinfo[i][0],".","."]
                    break
                else:
                    curr=tree[curr][1]
            #right
            else:
                if tree[curr][2]==".":
                    tree[curr][2]=nodeinfo[i][2]
                    tree[nodeinfo[i][2]]=[nodeinfo[i][0],".","."]
                    break
                else:
                    curr=tree[curr][2]
    pre(tree,root)
    post(tree,root)
    return answer

#nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
nodeinfo=[[1,1]]
print(solution(nodeinfo))