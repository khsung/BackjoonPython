#17413 단어 뒤집기2
input_string=input()
list_string=[]
if "<" in input_string:
    while input_string.count("<")>0:
        if input_string.index("<")==0:
            list_string.append(input_string[0:input_string.index(">")+1])
            input_string=input_string[input_string.index(">")+1:]
        else:
            list_string.append(input_string[:input_string.index("<")])
            input_string=input_string[input_string.index("<"):]
    if input_string!="":
        list_string.append(input_string)
else:
    list_string.append(input_string)
for i in range(len(list_string)):
    if list_string[i][0]=="<":
        print(list_string[i],end="")
    else:
        temp=list_string[i].split()
        for j in range(len(temp)):
            if j==len(temp)-1:
                print(temp[j][::-1],end="")
            else:
                print(temp[j][::-1],end=" ")