class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.child = []
        self.leaf = leaf


class BTree:
    def __init__(self):
        self.root = BTreeNode()

    def insert(self, key):
        root = self.root

        # Root is full
        if len(root.keys) == 2:
            new_root = BTreeNode(False)
            new_root.child.append(root)

            # Insert key first into the appropriate child
            if key < root.keys[0]:
                root.keys.insert(0, key)
            elif key > root.keys[-1]:
                root.keys.append(key)
            else:
                root.keys.insert(1, key)

            self.split(new_root, 0)
            self.root = new_root

        else:
            self.insert_non_full(root, key)

    def split(self, parent, index):
        old = parent.child[index]

        middle = old.keys[1]

        left = BTreeNode(old.leaf)
        right = BTreeNode(old.leaf)

        left.keys = [old.keys[0]]
        right.keys = [old.keys[2]]

        if not old.leaf:
            left.child = old.child[:2]
            right.child = old.child[2:]

        parent.keys.insert(index, middle)
        parent.child[index] = left
        parent.child.insert(index + 1, right)

    def insert_non_full(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1

            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1

            if len(node.child[i].keys) == 2:
                # Add key temporarily to child
                child = node.child[i]
                child.keys.append(key)
                child.keys.sort()

                self.split(node, i)

                return

            self.insert_non_full(node.child[i], key)

    def show(self, node=None):
        if node is None:
            node = self.root

        print(node.keys, end=" ")

        if not node.leaf:
            for c in node.child:
                self.show(c)


# Main program
tree = BTree()

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    tree.insert(value)

print("B-Tree:")
tree.show()