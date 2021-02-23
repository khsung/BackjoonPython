class Tree:
    def __init__(self,data,lchild,rchild):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild
tree=Tree(1,2,Tree(3,4,5))

print(tree.data)
print(tree.lchild)
print(tree.rchild.data)