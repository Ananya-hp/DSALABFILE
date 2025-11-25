

def bubble_sort(arr):
    n = len(arr)

  
    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



print("Bubble Sort Implementation")


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original List:", numbers)


sorted_list = bubble_sort(numbers)

print("Sorted List:", sorted_list)
