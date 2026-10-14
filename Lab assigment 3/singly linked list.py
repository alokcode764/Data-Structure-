class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
    # insert a elemnt into a index
    
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_head(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node.next = temp.next
        temp.next = new_node
        
    # Delete a element i a linke  dlist :
    
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Data not found")
        
     # dispaly element in a linked list :
     
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
sll = SinglyLinkedList()

n = int(input("How many values: "))

for i in range(n):
    value = int(input("Enter value: "))
    index = int(input("Enter index: "))

    sll.insert_at_index(value, index)

print("\nSingly Linked List:")
sll.display()

delete_value = int(input("\nEnter value to delete: "))
sll.delete(delete_value)

print("After deletion:")
sll.display()