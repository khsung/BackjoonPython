#5525 IOIOI
import sys
n=int(input())
p_n="IO"*n+"I"
m=int(input())
res=0
s=sys.stdin.readline().rstrip()
for i in range(m-2*n-1):
    if s[i:i+2*n+1]==p_n:
        res+=1
print(res)