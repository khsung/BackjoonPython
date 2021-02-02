#1541 잃어버린 괄호
expr_list = []
expr = input()
temp = ""
for i in range(len(expr)):
    if i == (len(expr) - 1):
        temp+=expr[i]
        expr_list.append(int(temp))
    else:
        if temp == "":
            temp = expr[i]
        elif expr[i] != "-" and expr[i] != "+":
            temp+=expr[i]
        else:
            expr_list.append(int(temp))
            expr_list.append(expr[i])
            temp = ""
while expr_list.count("+") != 0:
    expr_list[expr_list.index("+") - 1] = expr_list[expr_list.index("+") - 1] + expr_list[expr_list.index("+") + 1]
    del expr_list[expr_list.index("+") + 1]
    del expr_list[expr_list.index("+")]
while expr_list.count("-") != 0:
    expr_list[expr_list.index("-") - 1] = expr_list[expr_list.index("-") - 1] - expr_list[expr_list.index("-") + 1]
    del expr_list[expr_list.index("-") + 1]
    del expr_list[expr_list.index("-")]
print(*expr_list)