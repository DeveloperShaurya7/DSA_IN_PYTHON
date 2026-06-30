# Q. Given a string s count the frequency of each character and return the result.

def count_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

text = input("Enter a string: ")
frequency = count_frequency(text)
print("Character frequency:", frequency)

