#5430 AC
testcase=int(input())
for i in range(testcase):
    array=[]
    func=input()
    func=func.replace("RR","")
    checkR=False
    left=0
    right=0
    arraysize=int(input())
    temp=input()
    array=list(map(int,temp[1:-1].replace(","," ").split()))
    for j in range(len(func)):
        if func[j]=="R":
            if checkR==False:
                checkR=True
            else:
                checkR=False
        else:
            if checkR==False:
                left+=1
            else:
                right+=1
    if left+right>arraysize:
        print("error")
    else:
        if right==0:
            res=array[left:]
        else:
            res=array[left:-1*right]
        print("[",end="")
        if checkR==True:
            res.reverse()
        for j in range(len(res)):
            print(res[j],end="")
            if j!=len(res)-1:
                print(",",end="")
        print("]")