def quick_sort(lst):
    _quick_sort(lst, 0, len(lst)-1)

def _quick_sort(lst, first, last):
    if first < last:
        j = partition(lst, first, last)

        _quick_sort(lst, first, j-1)
        _quick_sort(lst, j+1, last)

def partition(lst, first, last):
    pvt = lst[first]

    i = first+1
    j = last
    while True:
        while i <= j and lst[i] <= pvt:
            i += 1
        while j >= i and lst[j] >= pvt:
            j -= 1
        if i > j:
            break
        else:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
    tmp = lst[first]
    lst[first] = lst[j]
    lst[j] = tmp

    return j
