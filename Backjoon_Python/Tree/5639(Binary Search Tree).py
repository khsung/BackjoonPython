#5639 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)

num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num)
    except:
        break

def postorder(left,right):
    mid=left
    if left+1<right:
        for i in range(left,right):
            print(num_list[left:right])
            if num_list[left]<num_list[i]:
                mid=i
                postorder(left+1,mid)
                break
            elif i==right-1:
                mid=right
                postorder(left+1,mid)
        postorder(mid,right)
    print("left =",left)
    print(num_list[left])

postorder(0,len(num_list))



#import sys
#sys.setrecursionlimit(10**6)

#binary_tree={}
#while True:
#    try:
#        num=int(input())
#        if len(binary_tree)==0:
#            root=num
#            binary_tree[root]=['*','*']
#        else:
#            curr=root
#            while True:
#                if num<curr:
#                    if binary_tree[curr][0]=='*':
#                        binary_tree[curr][0]=num
#                        binary_tree[num]=['*','*']
#                        break
#                    else:
#                        curr=binary_tree[curr][0]
#                else:
#                    if binary_tree[curr][1]=='*':
#                        binary_tree[curr][1]=num
#                        binary_tree[num]=['*','*']
#                        break
#                    else:
#                        curr=binary_tree[curr][1]
#    except:
#        break

#def postorder(curr):
#    if binary_tree[curr][0]!='*':
#        postorder(binary_tree[curr][0])
#    if binary_tree[curr][1]!='*':
#        postorder(binary_tree[curr][1])
#    print(curr)

#postorder(root)