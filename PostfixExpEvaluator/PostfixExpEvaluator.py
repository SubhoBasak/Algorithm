class Stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        return self.__items.pop()

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False

def evaluator(st):
    lst = list(st)
    return __evaluator(lst)

def __evaluator(lst):
    stack = Stack()
    for i in lst:
        if i in ['+', '-', '*', '/', '^']:
            if not stack.isEmpty():
                b = stack.pop()
                a = stack.pop()
                if i == '^':
                    i = '**'
                stack.push(str(eval(a+i+b)))
        else:
            stack.push(i)
    return float(stack.pop())
