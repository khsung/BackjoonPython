#11659 구간 합 구하기 4(미완성)
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
segmenttree=[0 for i in range(4*len(numbers))]
maxindex=0
def initsegment(left,right,index):
    global numbers, segmenttree,maxindex
    if left==right:
        segmenttree[index]=numbers[left]
        if left>maxindex:
            maxindex=left
        return segmenttree[index]
    else:
        mid=(left+right)//2
        segmenttree[index]=initsegment(left,mid,2*index)+initsegment(mid+1,right,2*index+1)
        return segmenttree[index]

initsegment(0,n-1,1)
print("segment =",segmenttree)
def segment(left,right,i,j,index):
    print("i,j =",i,j)
    print("left,right =",left,right)
    global segmenttree
    if left==i and right==j:
        return segmenttree[index]
    else:
        mid=(left+right)//2
        if j<=mid:
            return segment(left,mid,i,j,2*index)
        elif i>mid:
            return segment(mid+1,right,i,j,2*index+1)
        else:
            sum=segment(left,mid,i,j,2*index)+segment(mid+1,right,i,j,2*index+1)
            return sum

for i in range(m):
    a,b=map(int,input().split())
    print(segment(0,n-1,a-1,b-1,1))