#17269 이름궁합 테스트
alpha={'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1,}
n,m=map(int,input().split())
n_name,m_name=input().split()
n_name=list(n_name)
m_name=list(m_name)
total_name=[]
while len(n_name)>0 or len(m_name)>0:
    if len(n_name)>0:
        total_name.append(alpha[n_name.pop(0)])
    if len(m_name)>0:
        total_name.append(alpha[m_name.pop(0)])
while len(total_name)>2:
    for i in range(len(total_name)-1):
        total_name[i]=(total_name[i]+total_name[i+1])%10
    total_name.pop()
print(total_name[0]*10+total_name[1],end="")
print("%")