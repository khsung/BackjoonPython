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
    if left>right:
        return
    else:
        mid=right+1
        for i in range(left+1,right+1):
            if num_list[left]<num_list[i]:
                mid=i
                break
        postorder(left+1,mid-1)
        postorder(mid,right)
        print(num_list[left])

postorder(0,len(num_list)-1)



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