# Q. Give a string, count the frequency of each character.


def count_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

s = "programmming"
result = count_characters(s)

for char, count in result.items():
    print(f"Character: {char}, Frequency: {count}")