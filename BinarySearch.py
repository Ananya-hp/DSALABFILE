

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1



arr = []
n = int(input("Enter number of sorted elements: "))

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

key = int(input("Enter element to search: "))

print("Array:", arr)

pos = binary_search(arr, key)

if pos != -1:
    print(f"Element found at index {pos}")
else:
    print("Element not found")
