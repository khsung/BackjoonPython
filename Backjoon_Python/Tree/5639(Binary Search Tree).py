#5639 이진 검색 트리
queue=[]
dic={}
cnt=0
while True:
    try:
        cnt+=1
        temp=int(input())
        
        if cnt==1:
            dic[queue[0]]=[0,0]
            root=queue[0]
            queue.append(temp)
            parent=temp
        else:
            if temp<root:
                if parent>temp:
                    dic[parent][0]=temp
                    queue.append(temp)
                    parent=temp
                else:
                    while queue[len(queue)-2]<temp:
                        queue.pop()
                    dic[queue.pop()][1]=temp
        print(dic)

    except:
        break
