lst = input()
lst = lst.split(',')
lst = [int(i) for i in lst]
ln = len(lst)

for i in range(ln-1):
    indx = lst.index(max(lst[:ln-i]))
    tmp = lst[ln-i-1]
    lst[ln-i-1] = lst[indx]
    lst[indx] = tmp

print(lst)

