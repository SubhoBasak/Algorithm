# this radix sort is only for integer sorting
class queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, value):
        self.__items.append(value)

    def dequeue(self):
        return self.__items.pop(0)

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False

def radix_sort(lst):
    buc0 = queue()
    buc1 = queue()
    buc2 = queue()
    buc3 = queue()
    buc4 = queue()
    buc5 = queue()
    buc6 = queue()
    buc7 = queue()
    buc8 = queue()
    buc9 = queue()
 
    lst = list(map(str, lst))
    mx_d = 0
    for i in lst:
        if len(i)>mx_d:
            mx_d = len(i)
    for i in range(len(lst)):
        if len(lst[i])<mx_d:
            lst[i] = ((mx_d-len(lst[i]))*'0')+lst[i]
    for i in range(mx_d):
        for j, k in enumerate(lst):
            l = k[(mx_d-1-i)]
            if l == '0':
                buc0.enqueue(lst[j])
            elif l == '1':
                buc1.enqueue(lst[j])
            elif l == '2':
                buc2.enqueue(lst[j])
            elif l == '3':
                buc3.enqueue(lst[j])
            elif l == '4':
                buc4.enqueue(lst[j])
            elif l == '5':
                buc5.enqueue(lst[j])
            elif l == '6':
                buc6.enqueue(lst[j])
            elif l == '7':
                buc7.enqueue(lst[j])
            elif l == '8':
                buc8.enqueue(lst[j])
            else:
                buc9.enqueue(lst[j])
        for m in range(len(lst)):
            if not buc0.isEmpty():
                lst[m] = buc0.dequeue()
            elif not buc1.isEmpty():
                lst[m] = buc1.dequeue()
            elif not buc2.isEmpty():
                lst[m] = buc2.dequeue()
            elif not buc3.isEmpty():
                lst[m] = buc3.dequeue()
            elif not buc4.isEmpty():
                lst[m] = buc4.dequeue()
            elif not buc5.isEmpty():
                lst[m] = buc5.dequeue()
            elif not buc6.isEmpty():
                lst[m] = buc6.dequeue()
            elif not buc7.isEmpty():
                lst[m] = buc7.dequeue()
            elif not buc8.isEmpty():
                lst[m] = buc8.dequeue()
            elif not buc9.isEmpty():
                lst[m] = buc9.dequeue()
    lst = list(map(int, lst))
    return lst
