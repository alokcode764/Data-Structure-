class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert operation
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Find minimum value
def find_min(root):
    while root.left:
        root = root.left
    return root


# Delete operation
def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        # No left child
        if root.left is None:
            return root.right

        # No right child
        if root.right is None:
            return root.left

        # Two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Main program
root = None

n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input("Enter element: "))
    root = insert(root, data)

x = int(input("Enter element to delete: "))
root = delete(root, x)

print("Element deleted successfully")