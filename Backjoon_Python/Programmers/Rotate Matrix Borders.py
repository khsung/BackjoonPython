#행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    graph=[[i+1+columns*j for i in range(columns)]for j in range(rows)]
    for i in range(len(queries)):
        topr=queries[i][0]-1
        leftc=queries[i][1]-1
        bottomr=queries[i][2]-1
        rightc=queries[i][3]-1
        min_num=temp=graph[topr][leftc]
        for j in range(leftc,rightc):
            temp,graph[topr][j+1]=graph[topr][j+1],temp
            if temp<min_num:
                min_num=temp
        for j in range(topr,bottomr):
            temp,graph[j+1][rightc]=graph[j+1][rightc],temp
            if temp<min_num:
                min_num=temp
        for j in range(rightc,leftc,-1):
            temp,graph[bottomr][j-1]=graph[bottomr][j-1],temp
            if temp<min_num:
                min_num=temp
        for j in range(bottomr,topr,-1):
            temp,graph[j-1][leftc]=graph[j-1][leftc],temp
            if temp<min_num:
                min_num=temp
        
        answer.append(min_num)
    return answer

rows=[6,3,100]
columns=[6,3,97]
queries=[[[2,2,5,4],[3,3,6,6],[5,1,6,3]],[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]],[[1,1,100,97]]]
for i in range(len(rows)):
    print(solution(rows[i], columns[i], queries[i]))