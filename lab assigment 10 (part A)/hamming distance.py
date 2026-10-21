# Hamming Distance
def hamming_distance(a, x):
    n = a ^ x
    count = 0

    while n > 0:
        count += n & 1
        n >>= 1

    return count


def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # Sort by Hamming Distance, then by number
    arr.sort(key=lambda a: (hamming_distance(a, x), a))

    print(*arr)

t=int(input())

for _ in range(t):
    solve()

