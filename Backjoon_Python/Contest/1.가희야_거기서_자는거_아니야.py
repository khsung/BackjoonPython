# 1번 가희야 거기서 자는거 아니야
R,C=input().split()
R=int(R)
C=int(C)
Rg,Cg,Rp,Cp=input().split()
Rg=int(Rg)
Cg=int(Cg)
Rp=int(Rp)
Cp=int(Cp)
min_Rg=R
min_Cg=C
min_Rp=R
min_Cp=C
graph=[]
for i in range(R):
    temp_graph=list(input())
    graph.append(temp_graph)
for i in range(R):
    for j in range(C):
        if graph[i][j]=="G":
            if i<min_Rg:
                min_Rg=i
            elif j<min_Cg:
                min_Cg=j
        if graph[i][j]=="P":
            if i<min_Rp:
                min_Rp=i
            elif j<min_Cp:
                min_Cp=j
if min_Rg+Rg<min_Rp or min_Rg>min_Rp+Rp or min_Cg+Cg<min_Cp or min_Cg>min_Cp+Cp:
    print(0)
else:
    if min_Rg<min_Rp:
        min_R=min_Rp
    else:
        min_R=min_Rg
    if min_Cg<min_Cp:
        min_C=min_Cp
    else:
        min_C=min_Cg
    if graph[min_R][min_C]=="G":
        print(1)
    else:
        print(0)