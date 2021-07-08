#7662 이중 우선순위 큐
t=int(input())
for i in range(t):
    k=int(input())
    array=[]
    for j in range(k):
        op=input().split()
        if op[0]=='I':
            array.append(int(op[1]))
        else:
            if len(array)>0:
                if op[1]=='1':
                    array.remove(max(array))
                else:
                    array.remove(min(array))
    if len(array)==0:
        print("EMPTY")
    else:
        print(max(array),min(array))