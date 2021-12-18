#이진 탐색 트리 구현

#리스트로 구현
def list_insert(curr,num):
    if binary_tree[curr]=='*':
        binary_tree[curr]=num
    elif num<binary_tree[curr]:
        list_insert(2*curr,num)
    else:
        list_insert(2*curr+1,num)

def list_delete(curr,num):
    if binary_tree[curr]=='*':
        print("빈 트리")
    else:
        #삭제할 노드 찾기
        while curr<len(binary_tree) and binary_tree[curr]!=num:
            if num<binary_tree[curr]:
                curr*=2
            else:
                curr=curr*2+1
        parent=curr
        #자식 노드가 없을 때
        if 2*curr>=len(binary_tree) or (binary_tree[curr*2]=='*' and binary_tree[curr*2+1]=='*'):
            binary_tree[curr]='*'

        #오른쪽 자식 노드만 있을 때
        elif binary_tree[curr*2]=='*':
            curr=curr*2+1
            while curr<len(binary_tree) and binary_tree[curr]!='*':
                curr=curr*2
            binary_tree[parent]=binary_tree[curr]
            binary_tree[curr]='*'

        #왼쪽 자식 노드가 있을 때     
        else:
            curr=curr*2
            while curr<len(binary_tree) and binary_tree[curr]!='*':
                curr=curr*2+1
            binary_tree[parent]=binary_tree[curr]
            binary_tree[curr]='*'


#딕셔너리로 구현
def dic_insert(curr,num):
    global root
    if len(binary_tree)==0:
        root=num
        binary_tree[root]=['*','*']
    else:
        if num<curr:
            if binary_tree[curr][0]=='*':
                binary_tree[curr][0]=num
                binary_tree[num]=['*','*']
            else:
                dic_insert(binary_tree[curr][0],num)
        else:
            if binary_tree[curr][1]=='*':
                binary_tree[curr][1]=num
                binary_tree[num]=['*','*']
            else:
                dic_insert(binary_tree[curr][1],num)


def dic_delete(curr,num):
    global root
    if len(binary_tree)==0:
        print("빈 트리")
    else:
        #삭제할 노드 찾기
        while curr!=num:
            parent=curr
            if num<curr:
                curr=binary_tree[curr][0]
                dir=0
            else:
                curr=binary_tree[curr][1]
                dir=1

        #자식 노드가 없을 때
        if binary_tree[curr]==['*','*']:
            binary_tree[parent][dir]='*'
            del binary_tree[curr]

        #오른쪽 자식 노드만 있을 때
        elif binary_tree[curr][0]=='*':
            del_node=curr
            temp_parent=curr
            #오른쪽 자식 이동 후 왼쪽 자식이 없을 때까지 왼쪽 자식으로 이동
            curr=binary_tree[curr][1]
            while binary_tree[curr][0]!='*':
                temp_parent=curr
                curr=binary_tree[curr][0]
            binary_tree[parent][dir]=curr
            binary_tree[curr]=binary_tree[del_node]

            #삭제할 노드의 자식 노드일 경우
            if binary_tree[temp_parent][1]==curr:
                binary_tree[temp_parent][1]='*'
            else:
                binary_tree[temp_parent][0]=curr
            del binary_tree[del_node]

        #왼쪽 자식 노드가 있을 때
        else:
            del_node=curr
            temp_parent=curr
            #왼쪽 자식 이동 후 오른쪽 자식이 없을 때까지 오른쪽 자식으로 이동
            curr=binary_tree[curr][0]
            while binary_tree[curr][1]!='*':
                temp_parent=curr
                curr=binary_tree[curr][1]
            binary_tree[parent][dir]=curr
            binary_tree[curr]=binary_tree[del_node]

            #삭제할 노드의 자식 노드일 경우
            if binary_tree[temp_parent][0]==curr:
                binary_tree[temp_parent][0]='*'
            else:
                binary_tree[temp_parent][1]=curr
            del binary_tree[del_node]





#구조체로 구현
class Node:
    def __init__(self,num):
        self.data=num
        self.left=None
        self.right=None

class Binary_tree:
    def __init__(self):
        self.root=None

    def Node_insert(self,num):
        if self.root==None:
            self.root=Node(num)
        else:
            self.curr=self.root
            while True:
                if num<self.curr.data:
                    if self.curr.left==None:
                        self.curr.left=Node(num)
                        break
                    else:
                        self.curr=self.curr.left
                else:
                    if self.curr.right==None:
                        self.curr.right=Node(num)
                        break
                    else:
                        self.curr=self.curr.right

    def Node_delete(self,num):
        if self.root==None:
            print("빈 트리")
        else:
            self.curr=self.root
            parent=self.root
            del_check=True
            dir_left=True
            while self.curr.data!=num:
                parent=self.curr
                if num<self.curr.data:
                    if self.curr.left==None:
                        print("삭제할 노드가 없습니다.")
                        del_check=False
                        break
                    else:
                        self.curr=self.curr.left
                        dir_left=True
                else:
                    if self.curr.right==None:
                        print("삭제할 노드가 없습니다.")
                        del_check=False
                        break
                    else:
                        self.curr=self.curr.right
                        dir_left=False

            if del_check:
                if dir_left:
                    while self.curr.right!=None:
                        self.curr=self.curr.right
                else:
                    while self.curr.left!=None:
                        self.curr=self.curr.left
                if parent==self.curr:
                    del self.curr
                else:
                    parent.data=self.curr.data
                    del self.curr




#리스트로 구현
binary_tree=['*' for i in range(16)]
root=1
list_insert(root,6)
list_insert(root,3)
list_insert(root,1)
list_insert(root,9)
list_insert(root,7)
list_insert(root,4)
list_insert(root,8)
#print(binary_tree)
list_delete(root,4)
#print(binary_tree)
list_delete(root,8)
#print(binary_tree)


#딕셔너리로 구현
binary_tree={}
root=None
dic_insert(root,6)
dic_insert(root,3)
dic_insert(root,1)
dic_insert(root,9)
dic_insert(root,7)
dic_insert(root,4)
dic_insert(root,8)
print(binary_tree)
dic_delete(root,4)
print(binary_tree)
dic_delete(root,7)
print(binary_tree)


#구조체로 구현
Binary=Binary_tree()
Binary.Node_insert(6)
Binary.Node_insert(3)
Binary.Node_insert(1)
Binary.Node_insert(9)
Binary.Node_insert(7)
Binary.Node_insert(4)
Binary.Node_insert(8)
print(Binary.root.left.data)
Binary.Node_delete(3)
print(Binary.root.left.data)
#print(Binary.root.right.data)