#class Tree:
#    def __init__(self,data,lchild,rchild):
#        self.data=data
#        self.lchild=lchild
#        self.rchild=rchild
#tree=Tree(1,2,Tree(3,4,5))
#
#print(tree.data)
#print(tree.lchild)
#print(tree.rchild.data)
n=int(input())
res=[0,0]
for i in range(n):
    a=int(input())
    if a==1:
        res[1]+=1
    else:
        res[0]+=1
if res[0]>res[1]:
    print("J")
else:
    print("")
