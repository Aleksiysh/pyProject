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
    return eval(express)


print("введите количество аргументов")
lenArgs = int(input())
print("введите выражение")
expression = input()

for i in range(pow(2, lenArgs)):
    line = list("{0:b}".format(i).zfill(lenArgs))
    print(line, end=" ")
    # print(ex)
    print()
    print(exp(expression, line))


