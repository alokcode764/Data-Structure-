import time

# User input
n = int(input("Enter data size: "))

# Create data
arr = list(range(n))

# Start time
start_time = time.perf_counter()

# Nested loops - O(n^2)
count = 0

for i in range(n):
    for j in range(n):
        count += 1

# End time
end_time = time.perf_counter()

# Calculate time in microseconds
time_taken = (end_time - start_time) * 1_000_000

print("\nData Size:", n)
print("Total operations:", count)
print("Time taken:", time_taken, "microseconds")
print("Time Complexity: O(n^2)")