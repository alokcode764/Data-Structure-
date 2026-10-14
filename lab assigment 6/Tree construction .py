class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(int(input("Enter root: ")))

root.left = Node(int(input("Enter left child of root: ")))
root.right = Node(int(input("Enter right child of root: ")))

root.left.left = Node(int(input("Enter left child of left node: ")))
root.left.right = Node(int(input("Enter right child of left node: ")))

# Display Tree
print("\nBinary Tree:")
print("          ", root.data)
print("         /   \\")
print("        ↓     ↓")
print("       ", root.left.data, "   ", root.right.data)
print("      /   \\")
print("     ↓     ↓")
print("    ", root.left.left.data, "   ", root.left.right.data)