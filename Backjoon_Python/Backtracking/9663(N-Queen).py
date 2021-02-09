#9663 N-Queen (시간초과)

import time
num=int(input())
start = time.time()
nqueen=[]
count=0
def linechk(nqueen,row,col):
    for i in range(len(nqueen)):
        if (nqueen[i][1]==col) or abs(nqueen[i][0]-row)==abs(nqueen[i][1]-col):
            return 0
    return 1
def Nqueen(nqueen,cur,maxline):
    global count
    if cur==maxline:
        for i in range(1,maxline+1):
            if linechk(nqueen,cur,i):
                count+=1
    else:
        for i in range(1,maxline+1):
            if linechk(nqueen,cur,i):
                nqueen.append([cur,i])
                Nqueen(nqueen,cur+1,maxline)
                nqueen.pop()
Nqueen(nqueen,1,num)
print(count)
print("time :", time.time() - start)