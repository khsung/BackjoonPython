#1966 프린터 큐
import copy
testcase=int(input())
for i in range(testcase):
    n,m=map(int,input().split())
    printerqueue=list(map(int, input().split()))
    importance=copy.deepcopy(printerqueue)