# Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr

# Bucket Sort

def bucket_sort(arr):
    n = len(arr)

    if n == 0:
        return arr

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Put elements into buckets
    for value in arr:
        index = int(value * n)

        if index == n:
            index = n - 1

        buckets[index].append(value)

    # Sort each bucket
    for bucket in buckets:
        insertion_sort(bucket)

    # Combine all buckets
    result = []

    for bucket in buckets:
        for value in bucket:
            result.append(value)

    return result

# Main Program

print("===================================")
print("       SORTING ALGORITHMS")
print("===================================")

print("\n1. Insertion Sort")
print("2. Bucket Sort")

choice = int(input("\nEnter your choice: "))

if choice == 1:

    print("\n--- Insertion Sort ---")

    n = int(input("Enter number of elements: "))

    arr = []

    for i in range(n):
        value = int(input("Enter element: "))
        arr.append(value)

    print("\nOriginal Array:", arr)

    insertion_sort(arr)

    print("Sorted Array:", arr)


elif choice == 2:

    print("\n--- Bucket Sort ---")
    print("Enter decimal values between 0 and 1")

    n = int(input("Enter number of elements: "))

    arr = []

    for i in range(n):
        value = float(input("Enter element: "))

        if value < 0 or value > 1:
            print("Please enter a value between 0 and 1.")
            exit()

        arr.append(value)

    print("\nOriginal Array:", arr)

    sorted_array = bucket_sort(arr)

    print("Sorted Array:", sorted_array)


else:
    print("\nInvalid choice!")
    