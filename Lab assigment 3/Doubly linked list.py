class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
  

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a node at the end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Delete a node using its data
    def delete(self, data):
        current = self.head

        while current is not None:

            if current.data == data:

                # If deleting the first node
                if current == self.head:
                    self.head = current.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None

                # If deleting the last node
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # If deleting a middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                print("Node deleted successfully.")
                return

            current = current.next

        print("Node not found.")

    # Reverse traversal
    def reverse_traversal(self):
        current = self.tail

        print("Reverse Linked List:")

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


# Main program
dll = DoublyLinkedList()

n = int(input("How many values: "))

for i in range(n):
    value = int(input("Enter value: "))
    dll.insert(value)

print("\nReverse Traversal:")
dll.reverse_traversal()

value = int(input("\nEnter value to delete: "))
dll.delete(value)

print("\nReverse Traversal after deletion:")
dll.reverse_traversal()


