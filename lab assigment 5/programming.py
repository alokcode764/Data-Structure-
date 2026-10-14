#infix to postfix conversion
stack = []
postfix = ""

exp = input("Enter Infix Expression: ")

for ch in exp:

    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Postfix Expression:", postfix)

