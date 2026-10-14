class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree using user input
root = Node(int(input("Enter root: ")))

left = input("Enter left child of root (or -1): ")
if left != "-1":
    root.left = Node(int(left))

right = input("Enter right child of root (or -1): ")
if right != "-1":
    root.right = Node(int(right))


# Add children of left node
if root.left:
    left = input("Enter left child of " + str(root.left.data) + " (or -1): ")
    if left != "-1":
        root.left.left = Node(int(left))

    right = input("Enter right child of " + str(root.left.data) + " (or -1): ")
    if right != "-1":
        root.left.right = Node(int(right))


# Add children of right node
if root.right:
    left = input("Enter left child of " + str(root.right.data) + " (or -1): ")
    if left != "-1":
        root.right.left = Node(int(left))

    right = input("Enter right child of " + str(root.right.data) + " (or -1): ")
    if right != "-1":
        root.right.right = Node(int(right))


# Recursive Inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Recursive Preorder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Recursive Postorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Inorder
print("\n\nInorder:")
inorder(root)

# Preorder
print("\nPreorder:")
preorder(root)

# Postorder
print("\nPostorder:")
postorder(root)


