#2475 검증수
a,b,c,d,e=input().split()
a=int(a)%10
b=int(b)%10
c=int(c)%10
d=int(d)%10
e=int(e)%10
print((a*a+b*b+c*c+d*d+e*e)%10)