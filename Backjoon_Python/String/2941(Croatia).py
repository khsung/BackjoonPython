#크로아티아 알파벳

string=input()
count=0
i=0
while i<len(string):
    if string[i]=="c":
        if i+1 < len(string) and (string[i+1] == "=" or string[i+1] == "-"):
            count += 1
            i+=2
        else:
            i+=1
            count += 1
    elif string[i]=="s" or string[i]=="z":
        if i+1 < len(string) and string[i+1] == "=":
            count += 1
            i+=2
        else:
            i+=1
            count += 1
    elif string[i]=="d":
        if i+1 < len(string) and string[i+1] == "-":
            count += 1
            i+=2
        elif i+1 < len(string) and string[i+1] == "z":
            if i+2 < len(string) and string[i+2] == "=":
                count += 1
                i+=3
            else:
                i+=1
                count += 1
        else:
            i+=1
            count += 1

    elif string[i]=="l" or string[i]=="n":
        if i+1 < len(string) and string[i+1] == "j":
            count += 1
            i+=2
        else:
            i+=1
            count += 1
    else:
        i+=1
        count += 1

print(count)
