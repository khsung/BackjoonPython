#트리 순회 구현
def preorder(root):
    print(root,end=" ")                     #현재 노드 출력
    if binary_tree[root][0]!="*":           #왼쪽 자식 노드가 존재하면 이동
        preorder(binary_tree[root][0])
    if binary_tree[root][1]!="*":           #오른쪽 자식 노드가 존재하면 이동
        preorder(binary_tree[root][1])

def inorder(root):
    if binary_tree[root][0]!="*":
        inorder(binary_tree[root][0])
    print(root,end=" ")
    if binary_tree[root][1]!="*":
        inorder(binary_tree[root][1])

def postorder(root):
    if binary_tree[root][0]!="*":
        postorder(binary_tree[root][0])
    if binary_tree[root][1]!="*":
        postorder(binary_tree[root][1])
    print(root,end=" ")

root=3
binary_tree={3:[1,5],1:[0,2],0:['*','*'],2:['*','*'],5:[4,6],4:['*','*'],6:['*','*']}

print("전위 순회시작")
preorder(root)

print("\n\n중위 순회시작")
inorder(root)

print("\n\n전위 순회시작")
postorder(root)