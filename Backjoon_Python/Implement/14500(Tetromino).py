#14500 테트로미노
import sys
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

res=0
tetro=[[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]], 
[[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]], 
[[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]], 
[[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]], 
[[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]], 
[[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]], 
[[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]], 
[[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]], 
[[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]], 
[[0, 1], [0, 2], [-1, 1]]]

for i in range(n):
    for j in range(m):
        for k in range(len(tetro)):
            a_x,a_y,b_x,b_y,c_x,c_y=tetro[k][0][0]+i,tetro[k][0][1]+j,tetro[k][1][0]+i,tetro[k][1][1]+j,tetro[k][2][0]+i,tetro[k][2][1]+j
            if 0<=a_x<n and 0<=a_y<m and 0<=b_x<n and 0<=b_y<m and 0<=c_x<n and 0<=c_y<m:
                temp_sum=graph[i][j]+graph[a_x][a_y]+graph[b_x][b_y]+graph[c_x][c_y]
                if temp_sum>res:
                    res=temp_sum
print(res)