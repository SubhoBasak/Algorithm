lst = input()
lst = lst.split(',')
lst = [int(i) for i in lst]
ln = len(lst)

for i in range(1, ln):
    j = 1
    while j <= i:
        if lst[i]<lst[i-j]:
            tmp = lst[i]
            lst[i] = lst[i-j]
            lst[i-j] = tmp
            i = i-j
        else:
            j += 1

print(lst)
