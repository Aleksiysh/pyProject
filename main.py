def exp(express, arg):
    pass
    len_args = len(arg)
    if (len_args > 1):
        a = int(arg[0])
        b = int(arg[1])
    if (len_args > 2):
        c = arg[2]
    if (len_args > 3):
        d = arg[3]
    if (len_args > 4):
        e = arg[4]
    if (len_args > 5):
        f = arg[5]
    if (len_args > 6):
        g = arg[6]
    if (len_args > 7):
        h = arg[7]
    return eval(express)


args = ("a", "b", "c", "d", "e", "f", "g", "h")
print("введите количество аргументов не более 7")
lenArgs = int(input())
print("введите выражение в синтаксисе python")
print("например : (a or b) and not c")
expression = input()
sknf = ""
for i in range(pow(2, lenArgs)):
    line = list("{0:b}".format(i).zfill(lenArgs))
    #print(line, end=" ")
    #print()
    #print(exp(expression, line))
    if (exp(expression, line) == 0):
        sknf += "(" if (sknf == "") else " and ("
        for i in range(lenArgs):
            sknf += args[i] if (line[i] == "0") else "not " + args[i]
            sknf += " or " if (i < lenArgs - 1) else ")"
print("исходное выражение")
print(expression)
print("СКНФ")
print(sknf)
pass

