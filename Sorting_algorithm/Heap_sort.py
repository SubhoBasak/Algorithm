class heap:
    def __init__(self):
        self.__items = []

    def insert(self, value):
        if len(self.__items) == 0:
            self.__items.append(value)
        else:
            self.__items.append(value)
            self.__sort_bottom_up(len(self.__items)-1)

    def __sort_bottom_up(self, cur_indx):
        if cur_indx != 0:
            if cur_indx%2 == 0:
                p = int((cur_indx-2)/2)
                if self.__items[p] < self.__items[cur_indx]:
                    tmp = self.__items[cur_indx]
                    self.__items[cur_indx] = self.__items[p]
                    self.__items[p] = tmp
                    self.__sort_bottom_up(p)
            else:
                p = int((cur_indx-1)/2)
                if self.__items[p] < self.__items[cur_indx]:
                    tmp = self.__items[cur_indx]
                    self.__items[cur_indx] = self.__items[p]
                    self.__items[p] = tmp
                    self.__sort_bottom_up(p)

    def peek(self):
        if len(self.__items) != 0:
            tmp = self.__items[0]
            self.__items[0] = self.__items[len(self.__items)-1]
            self.__items.pop()
            self.__sort_top_down(0)
            return tmp

    def __sort_top_down(self, cur_indx):
        left = right = None
        if 2*cur_indx+1 < len(self.__items):
            left = int(2*cur_indx+1)
        if 2*cur_indx+2 < len(self.__items):
            right = int(2*cur_indx+2)

        if left != None and right != None:
            mx = self.__items.index(max(self.__items[left], self.__items[right]))
        elif left != None:
            mx = left
        elif right != None:
            mx = right
        else:
            return None
        if self.__items[cur_indx] < self.__items[mx]:
            tmp = self.__items[cur_indx]
            self.__items[cur_indx] = self.__items[mx]
            self.__items[mx] = tmp
            self.__sort_top_down(mx)

def heap_sort(lst):
    h = heap()
    for i in lst:
        h.insert(i)
    for i in range(len(lst)):
        lst[i] = h.peek()
