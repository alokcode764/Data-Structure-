# Stack using Dynamic Linked Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push():
    global top

    value = int(input("Enter element: "))

    new_node = Node(value)
    new_node.next = top
    top = new_node

    print(value, "pushed into stack")


def pop():
    global top

    if top is None:
        print("Stack is Empty")
    else:
        value = top.data
        top = top.next
        print(value, "popped from stack")
    
def display():
    if top is None:
        print("Stack is Empty")
    else:
        temp = top

        print("\n TOP")
        print("  ↓")

        while temp is not None:
            print("+-------+")
            print("|", f"{temp.data:^5}", "|")
            print("+-------+")

            if temp.next is not None:
                print("  ↓")
            else:
                print("  ↓")
                print("None")

            temp = temp.next

        print("BOTTOM")

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
        print("Program ended")
        break
    else:
        print("Invalid choice")

