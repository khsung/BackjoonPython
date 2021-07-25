#13251 조약돌 꺼내기
m=int(input())
m_list=list(map(int,input().split()))
k=int(input())
temp_res=0

def find_comb(a,b):
    if a<b:
        return 0
    else:
        tempa=a-1
        tempb=b-1
        for i in range(b-1):
            a=a*tempa
            tempa-=1
        for i in range(b-1):
            b=b*tempb
            tempb-=1
        return a//b

for i in m_list:
    temp_res+=find_comb(i,k)
print(round(temp_res/find_comb(sum(m_list),k),11))