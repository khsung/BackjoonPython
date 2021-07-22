#2042 구간 합 구하기
#n,m,k=map(int,input().split())
#segment=[0 for i in range(4*n)]
#arr=[]
#diffarr=[]
#maxindex=0
#def initsegment(left,right,arr,index):
#    global segment,maxindex
#    if left==right:
#        if right>maxindex:
#            maxindex=right
#        segment[index]=arr[left]
#        return segment[index]
#    else:
#        mid=(left+right)//2
#        segment[index]=initsegment(left,mid,arr,2*index)+initsegment(mid+1,right,arr,1+2*index)
#        return segment[index]

#def findsum(left,right,first,second,arr,index):
#    mid=(left+right)//2
#    if left==first and right==second:
#        return segment[index]
#    elif mid>=second:
#        return findsum(left,mid,first,second,arr,2*index)
#    elif mid<first:
#        return findsum(mid+1,right,first,second,arr,1+2*index)
#    else:
#        sum=findsum(left,mid,first,mid,arr,2*index)+findsum(mid+1,right,mid+1,second,arr,1+2*index)
#        return sum

#def update(left,right,posi,diff,index):
#    global segment
#    segment[index]+=diff
#    mid=(left+right)//2
#    if left==right:
#        return
#    elif mid>=posi:
#        return update(left,mid,posi,diff,2*index)
#    else:
#        return update(mid+1,right,posi,diff,2*index+1)

#for i in range(n):
#    temp=int(input())
#    arr.append(temp)
#initsegment(0,n-1,arr,1)

#for i in range(m+k):
#    a,b,c=map(int,input().split())
#    if a==1:
#        diff=c-arr[b-1]
#        arr[b-1]=c
#        update(0,n-1,b-1,diff,1)
#    else:
#        print(findsum(0,n-1,b-1,c-1,arr,1))

#연습

import sys

def init(left,right,index):
    global origin,segment
    if left==right:
        segment[index]=origin[left-1]
        return segment[index]
    else:
        mid=(left+right)//2
        segment[index]=init(left,mid,2*index)+init(mid+1,right,2*index+1)
        return segment[index]

def update(left,right,target,index,diff):
    global segment
    segment[index]+=diff
    if left==target and right==target:
        pass
    else:
        mid=(left+right)//2
        if mid>=target:
            return update(left,mid,target,2*index,diff)
        else:
            return update(mid+1,right,target,2*index+1,diff)

def findsum(left,right,start,end,index):
    global segment
    if left==start and right==end:
        return segment[index]
    else:
        mid=(left+right)//2
        if mid>=end:
            return findsum(left,mid,start,end,2*index)
        elif mid<start:
            return findsum(mid+1,right,start,end,2*index+1)
        else:
            temp_sum=findsum(left,mid,start,mid,2*index)+findsum(mid+1,right,mid+1,end,2*index+1)
            return temp_sum

n,m,k=map(int,sys.stdin.readline().split())
origin=[]
segment=[0 for i in range(4*n)]
left=1
right=n
init_index=1
for i in range(n):
    origin.append(int(sys.stdin.readline()))
init(left,right,init_index)
for i in range(m+k):
    command=list(map(int,sys.stdin.readline().split()))
    if command[0]==1:
        diff=command[2]-origin[command[1]-1]
        origin[command[1]-1]=command[2]
        update(left,right,command[1],init_index,diff)
    else:
        print(findsum(left,right,command[1],command[2],init_index))