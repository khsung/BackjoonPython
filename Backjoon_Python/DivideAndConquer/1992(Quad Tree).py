#1992 쿼드트리
num=int(input())
square=[]
res=[]
for i in range(num):
    temp=list(map(int,input()))
    square.append(temp)
def quad(rfirst,rsecond,cfirst,csecond):
    global square
    global res
    cnt0=cnt1=0
    
    for i in range(rfirst,rsecond+1):
        cnt0+=square[i][cfirst:csecond+1].count(0)
        cnt1+=square[i][cfirst:csecond+1].count(1)
    if cnt0==0:
        res.append(1)
    elif cnt1==0:
        res.append(0)
    else:
        res.append("(")
        rmid=(rfirst+rsecond)//2
        cmid=(cfirst+csecond)//2
        quad(rfirst,rmid,cfirst,cmid)
        quad(rfirst,rmid,cmid+1,csecond)
        quad(rmid+1,rsecond,cfirst,cmid)     
        quad(rmid+1,rsecond,cmid+1,csecond)
        res.append(")")
quad(0,num-1,0,num-1)
for i in range(len(res)):
    print(res[i],end="")