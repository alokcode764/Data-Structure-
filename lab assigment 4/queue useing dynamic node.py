# Queue using Dynamic Linked Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

def enqueue():
    global front, rear

    value = int(input("Enter element: "))

    new_node = Node(value)

    if front is None:
        front = new_node
        rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    print(value, "inserted into queue")

def dequeue():
    global front, rear

    if front is None:
        print("Queue is Empty")
    else:
        value = front.data
        front = front.next

        if front is None:
            rear = None

        print(value, "deleted from queue")

def display():
    if front is None:
        print("Queue is Empty")
    else:
        temp = front

        print("\nQueue:")
        print("FRONT →", end=" ")

        while temp is not None:
            print("[", temp.data, "]", end="")

            if temp.next is not None:
                print(" →", end=" ")

            temp = temp.next

        print(" ← REAR")

        while temp is not None:
            print(temp.data)
            temp = temp.next

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
        print("Program ended")
        break
    else:
        print("Invalid choice")
