class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

def create(st):
    try:
        operand = float(st)
        return node(operand)

    except ValueError:
        parentheses = 0
        for i, j in enumerate(st):
            if j == '(':
                parentheses += 1
            elif j == ')':
                if parentheses > 0:
                    parentheses -= 1
                else:
                    print('\'(\' is missing before \')\'')
                    return None
            elif (j == '+' or j == '-') and parentheses == 0:
                root = node(j)
                root.left_child = create(st[:i])
                root.right_child = create(st[i+1:])
                return root

        parentheses = 0
        for i, j in enumerate(st):
            if j == '(':
                parentheses += 1
            elif j == ')':
                if parentheses > 0:
                    parentheses -= 1
                else:
                    print('\'(\' is missing before \')\'')
                    return None
            elif (j == '*' or j == '/') and parentheses == 0:
                root = node(j)
                root.left_child = create(st[:i])
                root.right_child = create(st[i+1:])
                return root

        parentheses = 0
        for i, j in enumerate(st):
            if j == '(':
                parentheses += 1
            elif j == ')':
                if parentheses > 0:
                    parentheses -= 1
                else:
                    print('\'(\' is missing before \')\'')
                    return None
            elif (j == '^' or j == '**') and parentheses == 0:
                root = node(j)
                root.left_child = create(st[:i])
                root.right_child = create(st[i+1:])
                return root

        st = st.lstrip('(').rstrip(')')
        return create(st)
