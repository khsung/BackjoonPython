#16675 두 개의 손
hands=input().split()
if hands[0]==hands[1] and hands[2]==hands[3]:
    if hands[0]=="S":
        if hands[2]=="R":
            print("TK")
        elif hands[2]=="P":
            print("MS")
        else:
            print("?")
    elif hands[0]=="R":
        if hands[2]=="P":
            print("TK")
        elif hands[2]=="S":
            print("MS")
        else:
            print("?")
    else:
        if hands[2]=="S":
            print("TK")
        elif hands[2]=="R":
            print("MS")
        else:
            print("?")
elif hands[0]==hands[1]:
    if hands[0]=="S":
        if hands[2]=="R" or hands[3]=="R":
            print("TK")
        else:
            print("?")
    elif hands[0]=="R":
        if hands[2]=="P" or hands[3]=="P":
            print("TK")
        else:
            print("?")
    else:
        if hands[2]=="S" or hands[3]=="S":
            print("TK")
        else:
            print("?")
elif hands[2]==hands[3]:
    if hands[2]=="S":
        if hands[0]=="R" or hands[1]=="R":
            print("MS")
        else:
            print("?")
    elif hands[2]=="R":
        if hands[0]=="P" or hands[1]=="P":
            print("MS")
        else:
            print("?")
    else:
        if hands[0]=="S" or hands[1]=="S":
            print("MS")
        else:
            print("?")
else:
    print("?")