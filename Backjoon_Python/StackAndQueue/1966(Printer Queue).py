#1966 프린터 큐
import copy
testcase=int(input())
for i in range(testcase):
    n,m=map(int,input().split())
    printerqueue=list(map(int, input().split()))
    importance=copy.deepcopy(printerqueue)
    importance.sort(reverse=True)
    cnt=1
    res=cnt
    while len(printerqueue)>0:
        if importance[0]==printerqueue[0]:
            if m==0:
                res=cnt
                break
            else:
                importance.pop(0)
                printerqueue.pop(0)
                n-=1
                m-=1
                cnt+=1
                if m<0:
                    m+=n
        else:
            printerqueue.append(printerqueue.pop(0))
            m-=1
            if m<0:
                m+=n
    print(res)