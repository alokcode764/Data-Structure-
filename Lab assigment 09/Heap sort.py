# Heap Sort
def heapify(a, n, i):
    largest = i
    l, r = 2*i+1, 2*i+2

    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)

    # Build Max Heap
    for i in range(n//2-1, -1, -1):
        heapify(a, n, i)

    # Extract root repeatedly
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

a = [40, 10, 30, 5, 20, 15]
print("Before:", a)
heap_sort(a)
print("After Heap Sort:", a)