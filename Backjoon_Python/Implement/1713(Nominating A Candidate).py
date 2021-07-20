#1713 후보 추천하기
n=int(input())
m=int(input())
m_list=list(map(int,input().split()))
pic=[]
timer=1
for i in range(len(m_list)):
    if len(pic)==0:
        #후보 번호, 추천 횟수, 추천 시기
        pic.append([m_list[i],1,timer])
        timer+=1
    else:
        check=True
        for j in range(len(pic)):
            if pic[j][0]==m_list[i]:
                pic[j][1]+=1
                check=False
        if check:
            if len(pic)<n:
                pic.append([m_list[i],1,timer])
                timer+=1
            else:
                pic.sort(key=lambda x:(-x[1],-x[2]))
                pic[len(pic)-1]=[m_list[i],1,timer]
                timer+=1
pic.sort(key=lambda x:x[0])
for i in range(len(pic)):
    print(pic[i][0],end=" ")