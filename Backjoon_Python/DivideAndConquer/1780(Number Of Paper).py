#1780 종이의 개수
import sys
papernum=[0,0,0]
num=int(input())
paper=[]
for i in range(num):
    temp=list(map(int, sys.stdin.readline().split()))
    paper.append(temp)

def paperfunc(rfirst,rsecond,cfirst,csecond):
    global paper
    global papernum
    cnt_1=cnt0=cnt1=0
    for i in range(rfirst,rsecond+1):
        cnt_1+=paper[i][cfirst:csecond+1].count(-1)
        cnt0+=paper[i][cfirst:csecond+1].count(0)
        cnt1+=paper[i][cfirst:csecond+1].count(1)
    size=(rsecond+1-rfirst)*(csecond+1-cfirst)
    if size==cnt_1:
        papernum[0]+=1
    elif size==cnt0:
        papernum[1]+=1
    elif size==cnt1:
        papernum[2]+=1
    else:
        rthird=(rsecond+1-rfirst)//3
        cthird=(csecond+1-cfirst)//3
        paperfunc(rfirst,rfirst+rthird-1,cfirst,cfirst+cthird-1)
        paperfunc(rfirst,rfirst+rthird-1,cfirst+cthird,cfirst+2*cthird-1)
        paperfunc(rfirst,rfirst+rthird-1,cfirst+2*cthird,csecond)
        paperfunc(rfirst+rthird,rfirst+2*rthird-1,cfirst,cfirst+cthird-1)
        paperfunc(rfirst+rthird,rfirst+2*rthird-1,cfirst+cthird,cfirst+2*cthird-1)
        paperfunc(rfirst+rthird,rfirst+2*rthird-1,cfirst+2*cthird,csecond)
        paperfunc(rfirst+2*rthird,rsecond,cfirst,cfirst+cthird-1)
        paperfunc(rfirst+2*rthird,rsecond,cfirst+cthird,cfirst+2*cthird-1)
        paperfunc(rfirst+2*rthird,rsecond,cfirst+2*cthird,csecond)

paperfunc(0,num-1,0,num-1)
for i in range(3):
    print(papernum[i])