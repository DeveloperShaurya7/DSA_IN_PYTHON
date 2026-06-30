# Q. Write a program to reverse a string.
# def reverse_string(s):
#     return s[::-1]

# text = input("Enter a string: ")
# reversed_text = reverse_string(text)
# print("Reversed string:", reversed_text)



# Q. Write a program to reverse a string using a loop.

# def reverse_string_loop(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# text = input("Enter a string: ")
# reversed_text = reverse_string_loop(text)
# print("Reversed string:", reversed_text)


# Q. Write a program to reverse a string using two pointers.

def reverse_string(s):
    left = 0
    right = len(s) - 1
    s_list = list(s)  # Convert string to list for mutability

    while left < right:
        # Swap characters
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return ''.join(s_list)  # Convert list back to string


text = input("Enter a string: ")
reversed_text = reverse_string(text)

print("Reversed string:", reversed_text)


