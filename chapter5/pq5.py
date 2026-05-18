arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# A subarray is a contiguous part of an array. The maximum subarray problem is to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)