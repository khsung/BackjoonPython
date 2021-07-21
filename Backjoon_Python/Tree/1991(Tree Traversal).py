#1991 트리 순회
def preorder(trees,root):
    print(root,end="")
    if trees[root][0]!=".":
        preorder(trees,trees[root][0])
    if trees[root][1]!=".":
        preorder(trees,trees[root][1])

def inorder(trees,root):
    if trees[root][0]!=".":
        inorder(trees,trees[root][0])
    print(root,end="")
    if trees[root][1]!=".":
        inorder(trees,trees[root][1])

def postorder(trees,root):
    if trees[root][0]!=".":
        postorder(trees,trees[root][0])
    if trees[root][1]!=".":
        postorder(trees,trees[root][1])
    print(root,end="")

n=int(input())
trees={}
root="A"
for i in range(n):
    temp=input().split()
    trees[temp[0]]=[temp[1],temp[2]]

preorder(trees,root)
print()
inorder(trees,root)
print()
postorder(trees,root)