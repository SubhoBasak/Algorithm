lst = input().split(',')
lst = [int(i) for i in lst]
ln = len(lst)
gap = int(ln/2)

while gap != 0:
    cur = 0
    nxt = cur+gap
    while nxt < ln:
        if lst[cur] > lst[nxt]:
            tmp = lst[nxt]
            lst[nxt] = lst[cur]
            lst[cur] = tmp
        cur += 1
        nxt += 1
    gap = int(gap/2)

print(lst)
