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

def radix_sort(arr):
    SPACE = queue()
    A = queue()
    B = queue()
    C = queue()
    D = queue()
    E = queue()
    F = queue()
    G = queue()
    H = queue()
    I = queue()
    J = queue()
    K = queue()
    L = queue()
    M = queue()
    N = queue()
    O = queue()
    P = queue()
    Q = queue()
    R = queue()
    S = queue()
    T = queue()
    U = queue()
    V = queue()
    W = queue()
    X = queue()
    Y = queue()
    Z = queue()

    mx_ln = 0
    for i in arr:
        if len(i)>mx_ln:
            mx_ln = len(i)
    for i, j in enumerate(arr):
        if len(j)<mx_ln:
            arr[i] = j+(mx_ln-len(j))*' '
    for i in range(mx_ln):
        for k in arr:
            l = k[mx_ln-1-i]
            if l == ' ':
                SPACE.enqueue(k)
            elif l == 'A':
                A.enqueue(k)
            elif l == 'B':
                B.enqueue(k)
            elif l == 'C':
                C.enqueue(k)
            elif l == 'D':
                D.enqueue(k)
            elif l == 'E':
                E.enqueue(k)
            elif l == 'F':
                F.enqueue(k)
            elif l == 'G':
                G.enqueue(k)
            elif l == 'H':
                H.enqueue(k)
            elif l == 'I':
                I.enqueue(k)
            elif l == 'J':
                J.enqueue(k)
            elif l == 'K':
                K.enqueue(k) 
            elif l == 'L':
                L.enqueue(k)
            elif l == 'M':
                M.enqueue(k)
            elif l == 'N':
                N.enqueue(k)
            elif l == 'O':
                O.enqueue(k)
            elif l == 'P':
                P.enqueue(k)
            elif l == 'Q':
                Q.enqueue(k)
            elif l == 'R':
                R.enqueue(k)
            elif l == 'S':
                S.enqueue(k)
            elif l == 'T':
                T.enqueue(k)
            elif l == 'U':
                U.enqueue(k)
            elif l == 'V':
                V.enqueue(k)
            elif l == 'W':
                W.enqueue(k)
            elif l == 'X':
                X.enqueue(k) 
            elif l == 'Y':
                Y.enqueue(k)
            else:
                Z.enqueue(k)
        for k in range(len(arr)):
            if not SPACE.isEmpty():
                arr[k] = SPACE.dequeue()
            elif not A.isEmpty():
                arr[k] = A.dequeue()
            elif not B.isEmpty():
                arr[k] = B.dequeue()
            elif not C.isEmpty():
                arr[k] = C.dequeue()
            elif not D.isEmpty():
                arr[k] = D.dequeue()
            elif not E.isEmpty():
                arr[k] = E.dequeue()
            elif not F.isEmpty():
                arr[k] = F.dequeue()
            elif not G.isEmpty():
                arr[k] = G.dequeue()
            elif not H.isEmpty():
                arr[k] = H.dequeue()
            elif not I.isEmpty():
                arr[k] = I.dequeue()
            elif not J.isEmpty():
                arr[k] = J.dequeue()
            elif not K.isEmpty():
                arr[k] = K.dequeue()
            elif not L.isEmpty():
                arr[k] = L.dequeue()
            elif not M.isEmpty():
                arr[k] = M.dequeue()
            elif not N.isEmpty():
                arr[k] = N.dequeue()
            elif not O.isEmpty():
                arr[k] = O.dequeue()
            elif not P.isEmpty():
                arr[k] = P.dequeue()
            elif not Q.isEmpty():
                arr[k] = Q.dequeue()
            elif not R.isEmpty():
                arr[k] = R.dequeue()
            elif not S.isEmpty():
                arr[k] = S.dequeue()
            elif not T.isEmpty():
                arr[k] = T.dequeue()
            elif not U.isEmpty():
                arr[k] = U.dequeue()
            elif not V.isEmpty():
                arr[k] = V.dequeue()
            elif not W.isEmpty():
                arr[k] = W.dequeue()
            elif not X.isEmpty():
                arr[k] = X.dequeue()
            elif not Y.isEmpty():
                arr[k] = Y.dequeue()
            elif not Z.isEmpty():
                arr[k] = Z.dequeue()
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
