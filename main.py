# import operator

OPERATORS_LOGIC = {
    '!': [7, lambda x: 1 - x],
    '&': [6, lambda x, y: x if x < y else y],
    '|': [5, lambda x, y: x if x > y else y],
    '~': [4, lambda x, y: 1 if 1 < 1 - x + y else 1 - x + y],
}
OPERATORS_MATH = {
    '~': [7, lambda x: -x],
    '^': [7, lambda x, y: x ** y],
    '*': [6, lambda x, y,: x * y],
    '/': [6, lambda x, y: x / y],
    '+': [5, lambda x, y: x + y],
    '-': [5, lambda x, y: x - y],
}
OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

def parse(formula_string):
    number = ''
    for s in formula_string:
        if s in '1234567890.':  # если символ - цифра, то собираем число
            number += s
        elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            yield float(number)
            number = ''
        if s in OPERATORS or s in "()":  # если символ - оператор или скобка, то выдаём как есть
            yield s
    if number:  # если в конце строки есть число, выдаём его
        yield float(number)


def main():
    a = parse("2*5+5")
    print(a)
    pass
    # stack = []
    # stack.append('a')
    # stack.append('b')
    # stack.append('c')
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # # a = polska('1+4*3')
    pass


if __name__ == "__main__":
    main()
