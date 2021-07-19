#3425 고스택
def NUM_X(array,num):
    return array.append(num)

def POP(array):
    if len(array)==0:
        return "ERROR"
    else:
        return array.pop()

def INV(array):
    if len(array)==0:
        return "ERROR"
    else:
        temp=array.pop()
        return array.append(temp*(-1))

def DUP(array):
    if len(array)==0:
        return "ERROR"
    else:
        temp=array.pop()
        array.append(temp)
        return array.append(temp)

def SWP(array):
    if len(array)<2:
        return "ERROR"
    else:
        temp1=array.pop()
        temp2=array.pop()
        array.append(temp2)
        array.append(temp1)
        return array

def ADD(array):
    temp1=array.pop()
    temp2=array.pop()
    if abs(temp1+temp2)>10**9:
        return "ERROR"
    else:
        return array.append(temp1+temp2)

def SUB(array):
    if len(array)<2:
        return "ERROR"
    else:
        if abs(temp2-temp1)>10**9:
            return "ERROR"
        else:
            temp1=array.pop()
            temp2=array.pop()
            return array.append(temp2-temp1)

def MUL(array):
    temp1=array.pop()
    temp2=array.pop()
    if abs(temp1*temp2)>10**9:
        return "ERROR"
    else:
        return array.append(temp2*temp1)

def DIV(array):
    if len(array)<2:
        return "ERROR"
    else:
        op=1
        temp1=array.pop()
        temp2=array.pop()
        if temp1==0:
            return "ERROR"
        else:
            if temp1<0:
                op=op*(-1)
            if temp2<0:
                op=op*(-1)
            return array.append((abs(temp2)//abs(temp1))*op)

def MOD(array):
    if len(array)<2:
        return "ERROR"
    else:
        op=1
        temp1=array.pop()
        temp2=array.pop()
        if temp1==0:
            return "ERROR"
        else:
            if temp2<0:
                op=op*(-1)
            return array.append((abs(temp2)%abs(temp1))*op)

com="start"
res="start"
command_stack=[]
while com!="QUIT":
    com=input()
    if com=="END":
        num=int(input())
        for i in range(num):
            stack=[int(input())]
            for j in range(len(command_stack)):
                res="start"
                if len(command_stack[j].split())>1:
                    temp=command_stack[j].split()
                    NUM_X(stack,int(temp[1]))
                else:
                    if command_stack[j]=="POP":
                        res=POP(stack)
                    elif command_stack[j]=="INV":
                        res=INV(stack)
                    elif command_stack[j]=="DUP":
                        res=DUP(stack)
                    elif command_stack[j]=="SWP":
                        res=SWP(stack)
                    elif command_stack[j]=="ADD":
                        res=ADD(stack)
                    elif command_stack[j]=="SUB":
                        res=SUB(stack)
                    elif command_stack[j]=="MUL":
                        res=MUL(stack)
                    elif command_stack[j]=="DIV":
                        res=DIV(stack)
                    elif command_stack[j]=="MOD":
                        res=MOD(stack)
                if res=="ERROR":
                    print(res)
                    break
            if res!="ERROR":
                if len(stack)==1:
                    print(stack[0])
                else:
                    print("ERROR")
        command_stack.clear()
        print()
    elif com=="QUIT":
        pass
    else:
        command_stack.append(com)