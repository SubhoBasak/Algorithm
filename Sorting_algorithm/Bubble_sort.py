def bubble_sort(lst):
    ln = len(lst)
    for i in range(ln):
        print(i)
        m = 0
        for j in range(ln-1):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                m = 1
        if m == 0:
            break
    return lst
