import time
from unittest import result
def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

sizes = [10000, 50000, 100000] #size ia n array
print("\nbinary search, the time complexity analysis")
print("="*50)
   
for n in sizes:
    arr = list(range(n))
    target = int(input(f"Enter a target value to search in the array of size {n}: "))
    start = time.perf_counter()
    result, comparisons = binary_search(arr, target)
    end = time.perf_counter()

    time_taken = (end - start) * 1000000
    print("Array Size:", n)
    print("Target Value:", target)
    print("index found", result)
    print("Comparisons:", comparisons)
    print("Execution Time:", round(time_taken, 2), "microseconds")
    print("time complexity", "O(logn)")
    print("="*50)  
        
        
        
        