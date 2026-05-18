arr = [10, 20, 30, 40, 50]

target = 40

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}.")
        found = True
        break

    if not found:
        print(f"Element {target} not found in the array.")