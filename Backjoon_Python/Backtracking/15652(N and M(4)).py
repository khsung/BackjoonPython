#15652 N과M(4)
n,m=map(int, input().split())
visited=[0 for i in range(n)]
def printlist(array):
    for i in range(len(array)):
        print(array[i]+1,end=" ")
    print()
def backtracking(num,array,number,m):
    for i in range(num,n):
        array.append(i)
        if number==m-1:
            printlist(array)
            array.pop()
        else:
            backtracking(i,array,number+1,m)
            array.pop()
array=[]
backtracking(0,array,0,m)