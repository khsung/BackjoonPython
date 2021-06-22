#11054 가장 긴 바이토닉 부분 수열
n=int(input())
array=list(map(int,input().split()))
increase_seq=[0 for i in range(n)]
decrease_seq=[0 for i in range(n)]
increase_seq[0]=1
decrease_seq[n-1]=1
for i in range(1,n):
    max_value=0
    for j in range(i):
        if array[i]>array[j] and max_value<increase_seq[j]:
            max_value=increase_seq[j]
    increase_seq[i]=max_value+1

for i in range(n-2,-1,-1):
    max_value=0
    for j in range(n-1,i,-1):
        if array[i]>array[j] and max_value<decrease_seq[j]:
            max_value=decrease_seq[j]
    decrease_seq[i]=max_value+1

max_bio=0
for i in range(len(increase_seq)):
    if increase_seq[i]+decrease_seq[i]>max_bio:
        max_bio=increase_seq[i]+decrease_seq[i]
print(max_bio-1)