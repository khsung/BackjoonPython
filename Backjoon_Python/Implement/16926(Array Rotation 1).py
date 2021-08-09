#16926 배열 돌리기 1
n,m,r=map(int,input().split())
graph=[]
res=[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))

left_c=top_r=0
right_c=m-1
bottom_r=n-1
while left_c<right_c and top_r<bottom_r:
    curr_r=r%((right_c-left_c+1+bottom_r-top_r-1)*2)
    #위 가로
    for i in range(left_c,right_c+1):
        temp_r=curr_r
        if i-temp_r<left_c:
            temp_r-=(i-left_c)
            if top_r+temp_r>bottom_r:
                temp_r-=(bottom_r-top_r)
                if left_c+temp_r>right_c:
                    temp_r-=(right_c-left_c)
                    if bottom_r-temp_r<top_r:
                        temp_r-=(bottom_r-top_r)
                        res[top_r][right_c-temp_r]=graph[top_r][i]
                    else:
                        res[bottom_r-temp_r][right_c]=graph[top_r][i]
                else:
                    res[bottom_r][left_c+temp_r]=graph[top_r][i]
            else:
                res[top_r+temp_r][left_c]=graph[top_r][i]
        else:
            res[top_r][i-temp_r]=graph[top_r][i]

    #왼쪽 세로
    for i in range(top_r+1,bottom_r):
        temp_r=curr_r
        if i+temp_r>bottom_r:
            temp_r-=(bottom_r-i)
            if left_c+temp_r>right_c:
                temp_r-=(right_c-left_c)
                if bottom_r-temp_r<top_r:
                    temp_r-=(bottom_r-top_r)
                    if right_c-temp_r<left_c:
                        temp_r-=(right_c-left_c)
                        res[top_r+temp_r][left_c]=graph[i][left_c]
                    else:
                        res[top_r][right_c-temp_r]=graph[i][left_c]
                else:
                    res[bottom_r-temp_r][right_c]=graph[i][left_c]
            else:
                res[bottom_r][left_c+temp_r]=graph[i][left_c]
        else:
            res[i+temp_r][left_c]=graph[i][left_c]

    #아래 가로
    for i in range(left_c,right_c+1):
        temp_r=curr_r
        if i+temp_r>right_c:
            temp_r-=(right_c-i)
            if bottom_r-temp_r<top_r:
                temp_r-=(bottom_r-top_r)
                if right_c-temp_r<left_c:
                    temp_r-=(right_c-left_c)
                    if top_r+temp_r>bottom_r:
                        temp_r-=(bottom_r-top_r)
                        res[bottom_r][left_c+temp_r]=graph[bottom_r][i]
                    else:
                        res[top_r+temp_r][left_c]=graph[bottom_r][i]
                else:
                    res[top_r][right_c-temp_r]=graph[bottom_r][i]
            else:
                res[bottom_r-temp_r][right_c]=graph[bottom_r][i]
        else:
            res[bottom_r][i+temp_r]=graph[bottom_r][i]

    #오른쪽 세로
    for i in range(top_r+1,bottom_r):
        temp_r=curr_r
        if i-temp_r<top_r:
            temp_r-=(i-top_r)
            if right_c-temp_r<left_c:
                temp_r-=(right_c-left_c)
                if top_r+temp_r>bottom_r:
                    temp_r-=(bottom_r-top_r)
                    if left_c+temp_r>right_c:
                        temp_r-=(right_c-left_c)
                        res[bottom_r-temp_r][right_c]=graph[i][right_c]
                    else:
                        res[bottom_r][left_c+temp_r]=graph[i][right_c]
                else:
                    res[top_r+temp_r][left_c]=graph[i][right_c]
            else:
                res[top_r][right_c-temp_r]=graph[i][right_c]
        else:
            res[i-temp_r][right_c]=graph[i][right_c]

    left_c+=1
    top_r+=1
    right_c-=1
    bottom_r-=1

for i in range(n):
    for j in range(m):
        print(res[i][j],end=" ")
    print()