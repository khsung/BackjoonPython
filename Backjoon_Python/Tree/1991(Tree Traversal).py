#1991 트리 순회
def preorder(tree,root):
    print(root,end="")
    if tree[root][0]!=".":
        preorder(tree,tree[root][0])
    if tree[root][1]!=".":
        preorder(tree,tree[root][1])
    
def inorder(tree,root):
    if tree[root][0]!=".":
        inorder(tree,tree[root][0])
    print(root,end="")
    if tree[root][1]!=".":
        inorder(tree,tree[root][1])

def postorder(tree,root):
    if tree[root][0]!=".":
        postorder(tree,tree[root][0])
    if tree[root][1]!=".":
        postorder(tree,tree[root][1])
    print(root,end="")

n=int(input())
tree={}
for i in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]
    if i==0:
        saveroot=root

preorder(tree,saveroot)
print()
inorder(tree,saveroot)
print()
postorder(tree,saveroot)
