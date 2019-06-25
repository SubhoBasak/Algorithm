def change_i2po(st):
    lst = list(st)
    lst2 = []
    for i in lst:
        if i != ' ':
            lst2.append(i)
    tmp = __change_i2po(lst2)
    return tmp[0]

def __change_i2po(lst):
    p_start = None
    p_end = None
    count = 0
    for i, j in enumerate(lst):
        if j == '(':
            if p_start == None:
                p_start = i
            count += 1
        if j == ')':
            if p_start == None:
                print('Syntax error !\n) before (')
                return None
            else:
                count -= 1
                if count == 0:
                    p_end = i
                    break
            
    if p_start != None and p_end != None:
        tmp = __change_i2po(lst[p_start+1:p_end])
        lst = lst[:p_start]+tmp+lst[p_end+1:]
        return __change_i2po(lst)

    for i, j in enumerate(lst):
        if j == '^':
            lst[i] = lst[i-1]+' '+lst[i+1]+j
            lst.pop(i+1)
            lst.pop(i-1)
            lst = __change_i2po(lst)

    for i, j in enumerate(lst):
        if j == '*' or j == '/':
            lst[i] = lst[i-1]+' '+lst[i+1]+j
            lst.pop(i+1)
            lst.pop(i-1)
            lst = __change_i2po(lst)

    for i, j in enumerate(lst):
        if j == '+' or j == '-':
            lst[i] = lst[i-1]+' '+lst[i+1]+j
            lst.pop(i+1)
            lst.pop(i-1)
            lst = __change_i2po(lst)
    return lst

