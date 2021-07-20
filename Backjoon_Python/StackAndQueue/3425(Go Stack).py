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
        return array.append(temp1)

def ADD(array):
    if len(array)<2:
        return "ERROR"
    else:
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
        temp1=array.pop()
        temp2=array.pop()
        if abs(temp2-temp1)>10**9:
            return "ERROR"
        else:
            return array.append(temp2-temp1)

def MUL(array):
    if len(array)<2:
        return "ERROR"
    else:
        temp1=array.pop()
        temp2=array.pop()
        if abs(temp2*temp1)>10**9:
            return "ERROR"
        else:
            return array.append(temp2*temp1)

def DIV(array):
    if len(array)<2:
        return "ERROR"
    else:
        temp1=array.pop()
        temp2=array.pop()
        op=1
        if temp1==0:
            return "ERROR"
        else:
            if temp1<0:
                temp1=temp1*(-1)
                op=op*(-1)
            if temp2<0:
                op=op*(-1)
                temp2=temp2*(-1)
            return array.append((temp2//temp1)*op)

def MOD(array):
    if len(array)<2:
        return "ERROR"
    else:
        temp1=array.pop()
        temp2=array.pop()
        op=1
        if temp1==0:
            return "ERROR"
        else:
            if temp2<0:
                op=op*(-1)
                temp2=temp2*(-1)
            return array.append((temp2%abs(temp1))*op)

command="START"
command_array=[]
while command!="QUIT":
    command=input()
    if command=="QUIT":
        pass
    elif command=="END":
        n=int(input())
        for i in range(n):
            res="START"
            stack=[int(input())]
            for j in range(len(command_array)):
                if len(command_array[j].split())==2:
                    temp=command_array[j].split()
                    res=NUM_X(stack,int(temp[1]))
                elif command_array[j]=="POP":
                    res=POP(stack)
                elif command_array[j]=="INV":
                    res=INV(stack)
                elif command_array[j]=="DUP":
                    res=DUP(stack)
                elif command_array[j]=="SWP":
                    res=SWP(stack)
                elif command_array[j]=="ADD":
                    res=ADD(stack)
                elif command_array[j]=="SUB":
                    res=SUB(stack)
                elif command_array[j]=="MUL":
                    res=MUL(stack)
                elif command_array[j]=="DIV":
                    res=DIV(stack)
                else:
                    res=MOD(stack)
                if res=="ERROR":
                    break
            if res=="ERROR" or len(stack)!=1:
                print("ERROR")
            else:
                print(stack[0])
        input()
        print()
        command=="START"
        command_array.clear()
    else:
        command_array.append(command)