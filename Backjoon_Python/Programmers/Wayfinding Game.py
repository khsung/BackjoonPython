#길 찾기 게임
def solution(nodeinfo):
    answer = [[],[]]
    #tree={}
    #for i in range(len(nodeinfo)):
    #    nodeinfo[i].append(i+1)
    #nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    #tree[nodeinfo[0][2]]=[-1,-1]
    #curr=[[nodeinfo[0]]]
    #cur_parent=0
    #if len(nodeinfo)==1:
    #    answer=[[root],[root]]
    #else:
    #    for i in range(len(nodeinfo)-1):
    #        if nodeinfo[i+1][1]<curr[cur_parent][0][1]:
    #            cur_parent+=1
    #            curr.append([])
    #            curr[cur_parent].append(nodeinfo[i+1])
    #        else:
    #            curr[cur_parent].append(nodeinfo[i+1])
    #        check=True
    #        for j in range(len(curr[cur_parent-1])):
    #            if curr[cur_parent-1][0]>nodeinfo[i+1][0]:
    #                tree[curr[cur_parent-1][2]]=nodeinfo[i+1][2]
                    
    #                check=False
    #                break
    #        if check:


    return answer
nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))