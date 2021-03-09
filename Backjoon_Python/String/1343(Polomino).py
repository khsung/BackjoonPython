#1343 폴리오미노
temp=input()
temp=temp.replace("XXXX","AAAA")
temp=temp.replace("XX","BB")
if "X" in temp:
    print(-1)
else:
    print(temp)
