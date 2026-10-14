stack = []

exp = input("Enter Postfix Expression: ")

for ch in exp:

    if ch.isdigit():
        stack.append(int(ch))

    else:
        b = stack.pop()
        a = stack.pop()

        if ch == '+':
            stack.append(a + b)

        elif ch == '-':
            stack.append(a - b)

        elif ch == '*':
            stack.append(a * b)

        elif ch == '/':
            stack.append(a // b)

print("Result:", stack.pop())