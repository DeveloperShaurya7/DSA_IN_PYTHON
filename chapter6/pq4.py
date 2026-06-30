# Q. given two string s1 and s2 check whether they are anagrams of each other or not.


def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(s1) == sorted(s2)

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False