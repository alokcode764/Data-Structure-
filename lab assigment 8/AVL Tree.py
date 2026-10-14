class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    root.height = 1 + max(height(root.left), height(root.right))

    bf = balance(root)

    # LL
    if bf > 1 and data < root.left.data:
        return right_rotate(root)

    # RR
    if bf < -1 and data > root.right.data:
        return left_rotate(root)

    # LR
    if bf > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL
    if bf < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None
  
n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input("Enter value: "))
    root = insert(root, data)

print("AVL Tree:")
inorder(root)