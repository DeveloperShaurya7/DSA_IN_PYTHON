# Q. Give a string s and substring subs, write a Python function to check if subs is present in s. If it is present, return the index of the first occurrence of subs in s; otherwise, return -1.

def find_substring(s, subs):
    n = len(s)
    m = len(subs)
    for i in range(n - m + 1):
        if s[i:i + m] == subs:
            return i
        
    return -1

print(find_substring("hello world", "world"))  # Output: 6
print(find_substring("hello world", "python"))  # Output: -1

