# Queue using Array
MAX = 5
queue = [0] * MAX
front = -1
rear = -1

def enqueue():
    global front, rear

    if rear == MAX - 1:
        print("Queue is Full")
    else:
        value = int(input("Enter element: "))

        if front == -1:
            front = 0

        rear = rear + 1
        queue[rear] = value

        print(value, "inserted into queue")

def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue is Empty")
    else:
        value = queue[front]
        front = front + 1

        print(value, "deleted from queue")

        if front > rear:
            front = -1
            rear = -1

def display():
    if front == -1:
        print("Queue is Empty")
    else:
        print("Queue elements:")

        for i in range(front, rear + 1):
            print("+----+", end=" ")
        print()

        for i in range(front, rear + 1):
            print("|", queue[i], "|", end=" ")
        print()

        for i in range(front, rear + 1):
            print("+----+", end=" ")
        print()

        print("Front", end=" ")
        for i in range(front, rear + 1):
            print("     ", end=" ")
        print("Rear")

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
