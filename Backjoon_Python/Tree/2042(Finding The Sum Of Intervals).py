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

def initsegment(origin_numbers,segment_tree,curr_index,left,right):
    if left==right:
        segment_tree[curr_index]=origin_numbers[left-1]
        return segment_tree[curr_index]
    else:
        mid=(left+right)//2
        segment_tree[curr_index]=initsegment(origin_numbers,segment_tree,2*curr_index,left,mid)+initsegment(origin_numbers,segment_tree,2*curr_index+1,mid+1,right)
        return segment_tree[curr_index]

def update(segment_tree,curr_index,left,right,target_index,diff):
    mid=(left+right)//2
    segment_tree[curr_index]+=diff
    if left==right:
        return
    if mid>=target_index:
        return update(segment_tree,2*curr_index,left,mid,target_index,diff)
    else:
        return update(segment_tree,2*curr_index+1,mid+1,right,target_index,diff)


def findsum(segment_tree,curr_index,left,right,start,end):
    mid=(left+right)//2
    if left==start and right==end:
        return segment_tree[curr_index]
    elif mid>=end:
        return findsum(segment_tree,2*curr_index,left,mid,start,end)
    elif mid<start:
        return findsum(segment_tree,2*curr_index+1,mid+1,right,start,end)
    else:
        tempsum=findsum(segment_tree,2*curr_index,left,mid,start,mid)+findsum(segment_tree,2*curr_index+1,mid+1,right,mid+1,end)
        return tempsum
n,m,k=map(int,input().split())
origin_numbers=[]
start=1
end=n
segment_tree=[0 for i in range(4*n)]
for i in range(n):
    origin_numbers.append(int(input()))

initsegment(origin_numbers,segment_tree,1,start,end)
print(segment_tree)
for i in range(m+k):
    op=list(map(int,input().split()))
    if op[0]==1:
        update(segment_tree,1,start,end,op[1],op[2]-origin_numbers[op[1]-1])
    else:
        print(findsum(segment_tree,1,start,end,op[1],op[2]))
    print(segment_tree)