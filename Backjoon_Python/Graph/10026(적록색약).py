#10026 적록색약
size=int(input())
graph=[]
normalvisited=[[0 for i in range(size)]for j in range(size)]
normalcount=0
abnormalvisited=[[0 for i in range(size)]for j in range(size)]
abnormalcount=0

def cntfunc(i,j,color,state):
	global graph
	global normalvisited
	global abnormalvisited
	global size
	queue=[[i,j]]
	if state=="normal":
		while len(queue)>0:
			a=queue[0][0]
			b=queue[0][1]
			queue.pop(0)
			if a-1>=0 and normalvisited[a-1][b]==0 and graph[a-1][b]==color:
				normalvisited[a-1][b]=1
				queue.append([a-1,b])
			if b-1>=0 and normalvisited[a][b-1]==0 and graph[a][b-1]==color:
				normalvisited[a][b-1]=1
				queue.append([a,b-1])
			if a+1<size and normalvisited[a+1][b]==0 and graph[a+1][b]==color:
				normalvisited[a+1][b]=1
				queue.append([a+1,b])
			if b+1<size and normalvisited[a][b+1]==0 and graph[a][b+1]==color:
				normalvisited[a][b+1]=1
				queue.append([a,b+1])	
	else:
		if color=="B":
			while len(queue)>0:
				a=queue[0][0]
				b=queue[0][1]
				queue.pop(0)
				if a-1>=0 and abnormalvisited[a-1][b]==0 and graph[a-1][b]==color:
					abnormalvisited[a-1][b]=1
					queue.append([a-1,b])
				if b-1>=0 and abnormalvisited[a][b-1]==0 and graph[a][b-1]==color:
					abnormalvisited[a][b-1]=1
					queue.append([a,b-1])
				if a+1<size and abnormalvisited[a+1][b]==0 and graph[a+1][b]==color:
					abnormalvisited[a+1][b]=1
					queue.append([a+1,b])
				if b+1<size and abnormalvisited[a][b+1]==0 and graph[a][b+1]==color:
					abnormalvisited[a][b+1]=1
					queue.append([a,b+1])
		else:
			while len(queue)>0:
				a=queue[0][0]
				b=queue[0][1]
				queue.pop(0)
				if a-1>=0 and abnormalvisited[a-1][b]==0 and (graph[a-1][b]=='R' or graph[a-1][b]=='G'):
					abnormalvisited[a-1][b]=1
					queue.append([a-1,b])
				if b-1>=0 and abnormalvisited[a][b-1]==0 and (graph[a][b-1]=='R' or graph[a][b-1]=='G'):
					abnormalvisited[a][b-1]=1
					queue.append([a,b-1])
				if a+1<size and abnormalvisited[a+1][b]==0 and (graph[a+1][b]=='R' or graph[a+1][b]=='G'):
					abnormalvisited[a+1][b]=1
					queue.append([a+1,b])
				if b+1<size and abnormalvisited[a][b+1]==0 and (graph[a][b+1]=='R' or graph[a][b+1]=='G'):
					abnormalvisited[a][b+1]=1
					queue.append([a,b+1])

for i in range(size):
	temp=list(input())
	graph.append(temp)

for i in range(size):
	for j in range(size):
		if normalvisited[i][j]==0:
			normalvisited[i][j]=1
			cntfunc(i,j,graph[i][j],"normal")
			normalcount+=1
		if abnormalvisited[i][j]==0:
			abnormalvisited[i][j]=1
			cntfunc(i,j,graph[i][j],"abnormal")
			abnormalcount+=1
print(normalcount,abnormalcount)
