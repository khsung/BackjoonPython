#수식 최대화
import copy
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b

def ans(order_op,op_dic,exp_list):
    temp_exp=copy.deepcopy(exp_list)
    for i in range(len(order_op)):
        while order_op[i] in temp_exp:
            index=temp_exp.index(order_op[i])
            temp_exp[index-1]=op_dic[temp_exp[index]](temp_exp[index-1],temp_exp[index+1])
            del temp_exp[index]
            del temp_exp[index]
    return abs(temp_exp[0])

def solution(expression):
    answer = 0
    op=[]
    order_op=[]
    op_dic={}
    exp_list=[]
    last=0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            exp_list.append(int(expression[last:i]))
            exp_list.append(expression[i])
            last=i+1
            if expression[i] not in op:
                op.append(expression[i])
    exp_list.append(int(expression[last:]))
    for i in op:
        if i=="+":
            op_dic["+"]=plus
        elif i=="-":
            op_dic["-"]=minus
        else:
            op_dic["*"]=mul
    for i in range(len(op)):
        order_op.append(op[i])
        if len(op)==len(order_op):
            temp=ans(order_op,op_dic,exp_list)
            if temp>answer:
                answer=temp
        else:
            for j in range(len(op)):
                if op[j] not in order_op:
                    order_op.append(op[j])
                    if len(op)==len(order_op):
                        temp=ans(order_op,op_dic,exp_list)
                        if temp>answer:
                            answer=temp
                    else:
                        for k in range(len(op)):
                            if op[k] not in order_op:
                                order_op.append(op[k])
                                temp=ans(order_op,op_dic,exp_list)
                                if temp>answer:
                                    answer=temp
                                order_op.pop()
                    order_op.pop()
        order_op.pop()

    return answer

expression=["100-200*300-500+20","50*6-3*2","10*10"]

for i in range(len(expression)):
    print(solution(expression[i]))