# Optimal Merge Pattern

files = list(map(int, input("Enter file sizes: ").split()))
cost = 0

while len(files) > 1:
    files.sort()

    a = files.pop(0)
    b = files.pop(0)

    merge = a + b
    cost += merge

    print(a, "+", b, "=", merge)

    files.append(merge)

print("Minimum total cost:", cost)
