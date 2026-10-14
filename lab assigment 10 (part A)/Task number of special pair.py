# number of special pair:
def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


def solve():
    N = int(input("Enter number of elements: "))

    nums = list(map(int, input("Enter the values: ").split()))

    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            if digit_sum(nums[i]) == digit_sum(nums[j]):
                count += 1

    print("Number of special pairs:", count)
    


solve()