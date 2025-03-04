import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    """Implements a linear search on an array"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Implements a binary search on a sorted array"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Generate a larger sorted list of 100,000 elements
arr = list(range(1, 100001))
num_experiments = 100
linear_times = []
binary_times = []

for _ in range(num_experiments):
    target = random.randint(1, 100000)  # Pick a random number from the array

    # Time Linear Search
    start = time.perf_counter()
    linear_search(arr, target)
    linear_times.append(time.perf_counter() - start)

    # Time Binary Search
    start = time.perf_counter()
    binary_search(arr, target)
    binary_times.append(time.perf_counter() - start)

# Print sample execution times for verification
print("Linear Search times:", linear_times[:10])
print("Binary Search times:", binary_times[:10])

# Plot the results with more bins for better distinction
plt.figure(figsize=(10,5))
plt.plot(range(num_experiments), linear_times, label="Linear Search", marker='o', linestyle='-', color='blue')
plt.plot(range(num_experiments), binary_times, label="Binary Search", marker='s', linestyle='-', color='orange')
plt.xlabel("Experiment Number")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time per Experiment (Linear vs Binary Search)")
plt.legend()
plt.grid(True)
plt.show()

