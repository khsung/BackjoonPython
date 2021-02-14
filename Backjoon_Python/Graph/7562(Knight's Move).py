#7562 나이트의 이동
testcase=int(input())
def bfs(cnt):
    global chessvisited
    global destx
    global desty
    global knightlocation
    global chesssize
    queuesize=len(knightlocation)
    for i in range(queuesize):
        x=knightlocation[0][0]
        y=knightlocation[0][1]
        knightlocation.pop(0)
        if x==destx and y==desty:
            return cnt
        else:
            if x-2>=0 and y+1<chesssize and chessvisited[x-2][y+1]==0:
                chessvisited[x-2][y+1]=1
                knightlocation.append([x-2,y+1])
            if x-1>=0 and y+2<chesssize and chessvisited[x-1][y+2]==0:
                chessvisited[x-1][y+2]=1
                knightlocation.append([x-1,y+2])
            if x+1<chesssize and y+2<chesssize and chessvisited[x+1][y+2]==0:
                chessvisited[x+1][y+2]=1
                knightlocation.append([x+1,y+2])
            if x+2<chesssize and y+1<chesssize and chessvisited[x+2][y+1]==0:
                chessvisited[x+2][y+1]=1
                knightlocation.append([x+2,y+1])
            if x-2>=0 and y-1>=0 and chessvisited[x-2][y-1]==0:
                chessvisited[x-2][y-1]=1
                knightlocation.append([x-2,y-1])
            if x-1>=0 and y-2>=0 and chessvisited[x-1][y-2]==0:
                chessvisited[x-1][y-2]=1
                knightlocation.append([x-1,y-2])
            if x+1<chesssize and y-2>=0 and chessvisited[x+1][y-2]==0:
                chessvisited[x+1][y-2]=1
                knightlocation.append([x+1,y-2])
            if x+2<chesssize and y-1>=0 and chessvisited[x+2][y-1]==0:
                chessvisited[x+2][y-1]=1
                knightlocation.append([x+2,y-1])
    if len(knightlocation)>0:
        return bfs(cnt+1)

for i in range(testcase):
    chesssize=int(input())
    currx,curry=map(int,input().split())
    destx,desty=map(int,input().split())
    chessvisited=[[0 for i in range(chesssize)] for j in range(chesssize)]
    knightlocation=[[currx,curry]]
    chessvisited[currx][curry]=1
    print(bfs(0))