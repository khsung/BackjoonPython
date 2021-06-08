#16165 걸그룹 마스터 준석이
n,m=map(int,input().split())
quiz={}
for i in range(n):
    team_name=input()
    team_num=int(input())
    team_member=[]
    for j in range(team_num):
        team_member.append(input())
    quiz[team_name]=team_member

for i in range(m):
    quiz_name=input()
    quiz_type=int(input())
    if quiz_type==0:
        temp=quiz[quiz_name]
        temp.sort()
        for j in temp:
            print(j)
    else:
        for j in quiz:
            if quiz_name in quiz[j]:
                print(j)
                break