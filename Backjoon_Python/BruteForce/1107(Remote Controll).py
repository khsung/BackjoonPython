#1107 리모컨
n=input()
res=abs(100-int(n))
m=int(input())
if m != 0:
    m_list=list(map(int,input().split()))
else:
    m_list=[]
m_other_list=[]
for i in range(10):
    if i not in m_list:
        m_other_list.append(i)
temp_sum=0
clicked_num=""
if m==10:
    print(res)
else:
    for i in range(len(n)):
        if int(n[i]) not in m_list:
            clicked_num+=n[i]
        else:
            m_other_list.sort(key=lambda x:abs(int(n[i])-x))
            if m_other_list[0]==0:
                if len(m_other_list)>=2 and abs(m_other_list[0]-int(n[i]))==abs(m_other_list[1]-int(n[i])):
                    clicked_num+=str(m_other_list[1])
                else:
                    clicked_num+=str(m_other_list[0])
            else:
                clicked_num+=str(m_other_list[0])
        temp_sum+=1
    temp_sum+=abs(int(clicked_num)-int(n))
    if temp_sum<res:
        res=temp_sum

    print(res)