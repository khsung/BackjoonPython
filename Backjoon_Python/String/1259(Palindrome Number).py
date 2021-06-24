#1259 팰린드롬수
while True:
    string=input()
    if string=="0":
        break
    else:
        string=list(string)
        check=True
        while len(string)>0:
            if len(string)>1:
                left=string.pop(0)
                right=string.pop()
                if left!=right:
                    check=False
                    break
            else:
                string.pop()
        if check:
            print("yes")
        else:
            print("no")