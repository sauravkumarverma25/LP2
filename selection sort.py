def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        # Find the index of the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element in the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Take input from the user
arr = input("Enter elements of the array, separated by spaces: ").split()
arr = [int(num) for num in arr]

# Call selection_sort function
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
