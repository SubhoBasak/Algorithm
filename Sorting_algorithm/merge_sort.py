import math

def merge_sort(lst):
    split_point = math.ceil(len(lst)/2)
    if len(lst[:split_point]) > 1:
        left = merge_sort(lst[:split_point])
    else:
        left = lst[:split_point]
    if len(lst[split_point:]) > 1:
        right = merge_sort(lst[split_point:])
    else:
        right = lst[split_point:]
    return _merge_sort(left, right)

def _merge_sort(lst1, lst2):
    i = j = 0
    tmp_lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            tmp_lst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            tmp_lst.append(lst2[j])
            j += 1
        else:
            tmp_lst.append(lst1[i])
            tmp_lst.append(lst2[j])
            i += 1
            j += 1
    tmp_lst += lst1[i:]
    tmp_lst += lst2[j:]
    return tmp_lst
