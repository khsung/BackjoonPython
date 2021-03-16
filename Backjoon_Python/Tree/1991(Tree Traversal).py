#1991 트리 순회 미완성

def preorder(tree,root):
    print(root,end="")
    if tree[root][0]!=".":
        preorder(tree,tree[root][0])
    if tree[root][1]!=".":
        preorder(tree,tree[root][1])
    

def inorder(tree):
    return 0

def postorder(tree):
    return 0

n=int(input())
tree={}
for i in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]
    if i==0:
        saveroot=root
preorder(tree,saveroot)
print()

#temp={'A':[1,2]}
#print(temp['A'][0])