# Huffman Encoding

chars = input("Enter characters: ").split()
freq = list(map(int, input("Enter frequencies: ").split()))

nodes = [[freq[i], chars[i]] for i in range(len(chars))]

while len(nodes) > 1:
    nodes.sort()
    a = nodes.pop(0)
    b = nodes.pop(0)
    nodes.append([a[0] + b[0], [a[1], b[1]]])

codes = {}

def make_code(node, code=""):
    if isinstance(node, str):
        codes[node] = code or "0"
    else:
        make_code(node[0], code + "0")
        make_code(node[1], code + "1")

make_code(nodes[0][1])

print("Huffman Codes:")  
for ch in chars:
    print(ch, ":", codes[ch])
