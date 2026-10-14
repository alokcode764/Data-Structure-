# Stack using Static Array
MAX = 5
stack = [0] * MAX
top = -1

def push():
    global top

    if top == MAX - 1:
        print("Stack is Full")
    else:
        value = int(input("Enter element: "))
        top = top + 1
        stack[top] = value
        print(value, "pushed into stack")

def pop():
    global top

    if top == -1:
        print("Stack is Empty")
    else:
        value = stack[top]
        top = top - 1
        print(value, "popped from stack")

def display():
    if top == -1:
        print("Stack is Empty")
    else:
        print("\n TOP")
        print(" ↓")

        for i in range(top, -1, -1):
            print("+------+")

            print("|", end="")
            print(f"{stack[i]:^6}", end="")
            print("|")

        print("+------+")

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

