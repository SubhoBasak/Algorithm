import stack
stk = stack.stack()

def match(st):
    for j in st:
        if j == '(':
            stk.push(1)
        elif j == ')':
            if not stk.isEmpty():
                stk.pop()
            else:
                print('Mismatch error!\n\'(\' is missing')
                return False
    if stk.isEmpty():
        print('Paretheses are matched')
        return True
    else:
        print('Mismatch error!\n\')\' is missing')
        return False
