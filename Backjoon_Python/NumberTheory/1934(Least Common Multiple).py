#1934 최소공배수
import sys
sys.setrecursionlimit(10**6)
def find(a,b):
    if b%a==0:
        return a
    else:
        if b-a>a:
            return find(a,b-a)
        else:
            return find(b-a,a)
num_list=[]
num=int(input())
for i in range(num):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a>b:
        a,b=b,a
    temp=find(a,b)
    num_list.append(a*b//temp)
for i in range(len(num_list)):
    print(num_list[i])
