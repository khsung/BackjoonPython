#1931 회의실 배정
num=int(input())
meeting=[]
count=0
for i in range(num):
    a,b=input().split()
    meeting.append([int(a),int(b)])
meeting=sorted(meeting, key=lambda x:(x[1],x[0]))
for i in range(len(meeting)):
    if i==0:
        end=meeting[i][1]
        count+=1
    else:
        if meeting[i][0]>=end:
            end=meeting[i][1]
            count+=1
print(count)