import time
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):        
        comparisons += 1
    if arr[i] == target:
            return i, comparisons
    return -1, comparisons


sizes = [10000, 50000, 100000]
print("\nlinear search, the time complexity analysis")
print("="*50)
for n in sizes:
    arr = list(range(n))   
    target = int(input(f"Enter a target value to search in the array of size {n}:"))

    start = time.perf_counter()

    result, comparisons = linear_search(arr, target)

    end = time.perf_counter()

    time_taken = (end - start) * 1000000

    print("Array Size:", n)
    print("Target Value:", target)
    print("index found", result)
    print("Comparisons:", comparisons)
    print("Execution Time:", round(time_taken, 2), "microseconds")
    print("time complexity", "O(n)")
    print("="*50)
    