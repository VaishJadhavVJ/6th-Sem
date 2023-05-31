def selection_sort(arr):
    """
    Sorts the given array using the Selection Sort algorithm.
    """

    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted part of the array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Test the selection_sort function
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
