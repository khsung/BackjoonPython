#15650 N과M(2)
n,m=map(int, input().split())
visited=[0 for i in range(n)]
def printlist(array):
    for i in range(len(array)):
        print(array[i]+1,end=" ")
    print()
def backtracking(array,number,m,start):
    for i in range(start,len(visited)):
        if visited[i]==0 and number<m:
            array.append(i)
            visited[i]=1
            if len(array)==m:
                printlist(array)        
            backtracking(array,number+1,m,i+1)
            visited[i]=0
            array.pop()
array=[]
backtracking(array,0,m,0)