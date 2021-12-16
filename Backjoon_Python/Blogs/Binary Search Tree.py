#이진 탐색 트리 구현

#리스트로 구현
def list_insert(curr,num):
    if binary_tree[curr]=='*':
        binary_tree[curr]=num
    elif num<binary_tree[curr]:
        list_insert(2*curr,num)
    else:
        list_insert(2*curr+1,num)






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










binary_tree=['*' for i in range(16)]
root=1
list_insert(root,6)
list_insert(root,3)
list_insert(root,1)
list_insert(root,9)
list_insert(root,7)
list_insert(root,4)
list_insert(root,8)
print(binary_tree)


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


#구조체로 구현