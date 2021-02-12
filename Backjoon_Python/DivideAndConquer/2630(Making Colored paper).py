#2630 색종이 만들기
square = []
color = [0,0]
num = int(input())
for i in range(num):
    temp = list(map(int,input().split()))
    square.append(temp)

def squarefunc(rfirst,rsecond,cfirst,csecond):
    global square
    global color
    whitesum=0
    bluesum=0
    for i in range(rfirst,rsecond+1):
        temp=square[i][cfirst:csecond+1].count(0)
        whitesum+=temp
        bluesum=bluesum+(csecond+1-cfirst)-temp
    if bluesum==0:
        color[0]+=1
        return
    elif whitesum==0:
        color[1]+=1
        return
    else:
        rmid=(rfirst+rsecond)//2
        cmid=(cfirst+csecond)//2
        squarefunc(rfirst,rmid,cfirst,cmid)
        squarefunc(rfirst,rmid,cmid+1,csecond)
        squarefunc(rmid+1,rsecond,cfirst,cmid)
        squarefunc(rmid+1,rsecond,cmid+1,csecond)
squarefunc(0,num - 1,0,num - 1)
print(color[0])
print(color[1])