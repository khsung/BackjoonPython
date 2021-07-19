#1713 후보 추천하기
n=int(input())
m=int(input())
m_list=list(map(int,input().split()))
pic=[]
for i in range(len(m_list)):
    if len(pic)==0:
        pic.append([m_list[i],1])
    elif len(pic)<n:
        check=True
        for j in range(len(pic)):
            if pic[j][0]==m_list[i]:
                pic[j][1]+=1
                check=False
        if check:
            pic.append([m_list[i],1])
    else:
        check=True
        for j in range(len(pic)):
            if pic[j][0]==m_list[i]:
                pic[j][1]+=1
                check=False
        if check:
            pic.sort(key=lambda x:x[1])
            temp=len(pic)-1
            while temp-1>=0 and pic[temp][1]==pic[temp-1][1]:
                temp-=1
            del pic[temp]
            pic.append([m_list[i],1])
pic.sort(key=lambda x:x[0])
for i in range(len(pic)):
    print(pic[i][0],end=" ")