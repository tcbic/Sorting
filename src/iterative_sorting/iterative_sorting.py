# TO-DO: Complete the selection_sort() function below.

def selection_sort(arr):
    """The minimum element for a given iteration in the unsorted 
    portion of the array/list is placed in that given position in the sorted portion
    of the list. This continues until the entire list has been sorted."""

    # Loop through n-1 elements.
    # We dont't need to perform a comparison when we only have one item
    # left in the list, hence len(arr) - 1. We can assume it's the last value because
    # it's the only item left.

    for i in range(0, len(arr) - 1):
        # We want the first element in the unsorted list to be the default min.
        # We need that default to do the comparisons.
        cur_index = i
        # Set the minimum value to the current index.
        min_value = cur_index
        # For all the elements to the right of the current index...
        for b in range(i+1, len(arr)):
            # If we find an element smaller than the current index, replace
            # that current index value with b.
            if arr[b] < arr[cur_index]:
                cur_index = b
        # Perform the swap.
        if cur_index != min_value:
            arr[cur_index], arr[min_value] = arr[min_value], arr[cur_index]
        
    return arr

# Example
a = [13, 22, 3, 8, 5, 4, 1, 10, 19]
selection_sort(a)
print(a)

# TO-DO:  Implement the Bubble Sort function below.

def bubble_sort(arr):
    """The idea of the bubble sort algorithm is to move the higher valued
    elements generally towards the right and lower value elements generally
    toward the left."""
    #  Inlcude - 1 as we can't perform a comparison on the last element of the array.
    index_length = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for a in range(0, index_length):
            # If the value to the left is greater than the value on the right...
            if arr[a] > arr[a+1]:
                # Then the sorted variable is False, and...
                # This will not activate if all elements in the list have been sorted.
                sorted = False
                # swap those two values in the list.
                arr[a], arr[a+1] = arr[a+1], arr[a]

    return arr

# Example
b = [13, 22, 3, 8, 5, 4, 1, 10, 19]
bubble_sort(b)
print(b)

# STRETCH: Implement the Count Sort function below.
def count_sort(arr, maximum=-1):

    return arr