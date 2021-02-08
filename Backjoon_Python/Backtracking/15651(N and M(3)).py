#15651 N과M(3)
n,m=map(int, input().split())
visited=[0 for i in range(n)]
def printlist(array):
    for i in range(len(array)):
        print(array[i]+1,end=" ")
    print()
def backtracking(array,number,m):
    for i in range(n):
        array.append(i)
        if number==m-1:
            printlist(array)
            array.pop()
        else:
            backtracking(array,number+1,m)
            array.pop()
array=[]
backtracking(array,0,m)