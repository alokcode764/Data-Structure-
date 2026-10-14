# Open Hashing and Closed Hashing
class OpenHash:
    def __init__(self, size):
        self.table = [[] for _ in range(size)]
        self.size = size

    def insert(self, key):
        self.table[key % self.size].append(key)

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


class ClosedHash:
    def __init__(self, size=5):
        self.size = size
    
        self.table = [None] * size

    def insert(self, key):
        i = key % self.size
        while self.table[i] is not None:
            i = (i + 1) % self.size
        self.table[i] = key

    def rehash(self):
        old = self.table
        self.size *= 2
        self.table = [None] * self.size
        for key in old:
            if key is not None:
                self.insert(key)

    def display(self):
        print(self.table)


print("Open Hashing:")
h1 = OpenHash(5)
for x in [10, 15, 20, 7]:
    h1.insert(x)
h1.display()

print("\nClosed Hashing:")
h2 = ClosedHash()
for x in [10, 15, 20, 7]:
    h2.insert(x)
h2.rehash()
h2.display()