#1735 분수 합
a,b=map(int,input().split())
c,d=map(int,input().split())
top=a*d+c*b
bot=b*d
if top>bot:
    big=top
    small=bot
else:
    big=bot
    small=top

while small!=0:
    temp=big%small
    big,small=small,temp
print(top//big,bot//big)