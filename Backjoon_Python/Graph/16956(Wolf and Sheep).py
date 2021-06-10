#16956 늑대와 양
R,C=map(int,input().split())
graph=[]
check=True
for i in range(R):
    temp=list(input().replace(".","D"))
    graph.append(temp)

for i in range(R):
    if check==False:
        break
    for j in range(C):
        if graph[i][j]=="W":
            if i-1>=0 and graph[i-1][j]=="S":
                check=False
            elif i+1<R and graph[i+1][j]=="S":
                check=False
            elif j-1>=0 and graph[i][j-1]=="S":
                check=False
            elif j+1<C and graph[i][j+1]=="S":
                check=False
            if check==False:
                break
if check:
    print(1)
    for i in range(R):
        for j in range(C):
            print(graph[i][j],end="")
        print()
else:
    print(0)