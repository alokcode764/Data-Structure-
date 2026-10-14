class Heap:
    def __init__(self, is_min=True):
        self.a = []
        self.min = is_min

    def better(self, x, y):
        return x < y if self.min else x > y

    def push(self, x):
        self.a.append(x)
        i = len(self.a) - 1

        while i:
            p = (i - 1) // 2
            if self.better(self.a[i], self.a[p]):
                self.a[i], self.a[p] = self.a[p], self.a[i]
                i = p
            else:
                break

    def pop(self):
        root = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        i = 0

        while True:
            l, r = 2*i+1, 2*i+2
            best = i

            if l < len(self.a) and self.better(self.a[l], self.a[best]):
                best = l
            if r < len(self.a) and self.better(self.a[r], self.a[best]):
                best = r

            if best == i:
                break
            self.a[i], self.a[best] = self.a[best], self.a[i]
            i = best
        return root

x = list(map(int, input("Enter numbers: ").split()))

for mode in [True, False]:
    h = Heap(mode)
    for n in x:
        h.push(n)
    print("Min Heap:" if mode else "Max Heap:", h.a)