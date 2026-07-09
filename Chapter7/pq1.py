# Q. Given an array of integers, print the function of each element.

# arr = [1, 2, 2, 3, 1, 4, 2]


def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for key, value in freq.items():
        print(f"Element: {key}, Frequency: {value}")

    # return freq - use if you want to return the frequency dictionary instead of printing it

arr = [1, 2, 2, 3, 1, 4, 2, 5, 5, 6, 7]
print(count_frequency(arr))

# Time complexity - O(n)
# Space complexity - O(n)