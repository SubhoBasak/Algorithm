class stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        return self.__items.pop()

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False
