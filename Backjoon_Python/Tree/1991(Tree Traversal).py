#1991 트리 순회 미완성, 다른 트리 구현 방법 생각
#class Tree():
#    def __init__(self, parent,lchild=None,rchild=None):

n=int(input())
for i in range(n):
    parent,lchild,rchild=input().split()
    if lchild=='.':
        lchild=None
    if rchild=='.':
        rchild=None

    