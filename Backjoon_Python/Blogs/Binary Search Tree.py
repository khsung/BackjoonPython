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

        #자식 노드가 없을 때
        if curr<=len(binary_tree) or (binary_tree[curr*2]=='*' and binary_tree[curr*2+1]=='*'):
            binary_tree[curr]='*'

        #오른쪽 자식 노드만 있을 때
        elif binary_tree[curr*2]=='*':                                  
            parent=curr
            curr=curr*2+1
            while curr<len(binary_tree) and binary_tree[curr]!='*':
                curr=curr*2
            binary_tree[parent]=binary_tree[curr]
            binary_tree[curr]='*'

        #왼쪽 자식 노드가 있을 때     
        else:                                                           
            parent=curr
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
            parent=curr
            curr=binary_tree[curr][1]
            while binary_tree[curr][0]!='*':
                curr=binary_tree[curr][0]
            pass

        #왼쪽 자식 노드가 있을 때
        else:
            pass





#구조체로 구현




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
