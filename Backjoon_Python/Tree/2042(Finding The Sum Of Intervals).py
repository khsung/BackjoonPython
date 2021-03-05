#2042 구간 합 구하기
n,m,k=map(int,input().split())
segment=[0 for i in range(4*n)]
arr=[]
diffarr=[]
maxindex=0
def initsegment(left,right,arr,index):
    global segment,maxindex
    if left==right:
        if right>maxindex:
            maxindex=right
        segment[index]=arr[left]
        return segment[index]
    else:
        mid=(left+right)//2
        segment[index]=initsegment(left,mid,arr,2*index)+initsegment(mid+1,right,arr,1+2*index)
        return segment[index]

def findsum(left,right,first,second,arr,index):
    mid=(left+right)//2
    if left==first and right==second:
        return segment[index]
    elif mid>=second:
        return findsum(left,mid,first,second,arr,2*index)
    elif mid<first:
        return findsum(mid+1,right,first,second,arr,1+2*index)
    else:
        sum=findsum(left,mid,first,mid,arr,2*index)+findsum(mid+1,right,mid+1,second,arr,1+2*index)
        return sum

def update(left,right,posi,diff,index):
    segment[index]+=diff
    mid=(left+right)//2
    if left==right:
        return
    elif mid>=posi:
        return update(left,mid,posi,diff,2*index)

for i in range(n):
    temp=int(input())
    arr.append(temp)
initsegment(0,n-1,arr,1)

for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-arr[b-1]
        print(segment)
        #변경
    else:
        #출력
        print(findsum(0,n-1,b-1,c-1,arr,1))
