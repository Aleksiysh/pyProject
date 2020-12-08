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


def Tokens(str):
    operators = set(){"&&","-","*",}
    tokens = []
    return Lis


def main():
    OPERATORS = OPERATORS_MATH
    print(OPERATORS['^'][1](2, 0.5))

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
