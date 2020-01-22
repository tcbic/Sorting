# TO-DO: Complete the helper function below to merge 2 sorted arrays.

# From CS25 Lecture

# Step 1: Split our list into sub-lists until they are all length 1 or less.
def merge_sort(arr):
    # Check if it's length 1 or less. If so, return the list.
    # Any array that is length 1 or 0 is already sorted.
    # BASE CASE
    if len(arr) <= 1:
        return arr
    # Divide in half.
    left = arr[ : len(arr) // 2]
    right = arr[len(arr) // 2 : ]
    # Sort the left.
    left = merge_sort(left)
    # Sort the right.
    right = merge_sort(right)
    # Merge left and right together.
    return merge(left, right)

# Step 2: Merge the sorted sublists and return the sorted merged list.
def merge(arr_a, arr_b):
    total_elements = len(arr_a) + len(arr_b)
    merged_arr = [None] * total_elements
    # Counters to mark where we are in each list.
    a = 0
    b = 0
    for i in range (total_elements):
        # Check if either list is empty. If so, append the other.
        if a >= len(arr_a):
            merged_arr[i] = arr_b[b]
        elif b >= len(arr_b):
            merged_arr[i] = arr_a[a]
        # Otherwise, compare and append the smallest of the two.
        elif arr_a[a] < arr_b[b]:
            merged_arr[i] = arr_a[a]
            a += 1
        else:
            merged_arr[i] = arr_b[b]
            b += 1
    return merged_arr

# Slightly different writing of merge and merge_sort.

def merge2(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i=0
    j=0
    k=0
    while (i < len(arrA)) and (j < len(arrB)):
        
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            # Increment k and i to the next position.
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            # Increment k and j to the next position.
            k += 1
            j += 1
    while i < len(arrA):        
        merged_arr[k] = arrA[i]
        # Increment k and i to the next position.
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        # Increment k and j to the next position.
        k += 1
        j += 1

    return merged_arr

# TO-DO: Implement the merge_sort function below USING RECURSION!

def merge_sort2(arr):
    # What is the base case, the condition under which this algorithm
    # does not need to run?
    if len(arr) == 1:
        return arr
    # To split the array in half, take the length of the array and divide
    # by two.
    else:
        half = len(arr) // 2
        # Define the two separate halves.
        part_a = arr[:half] 
        part_b = arr[half:]
        # Use merge as defined above and use recursion to sort the array.
        arr = merge2(merge_sort2(part_a), merge_sort2(part_b))
        return arr

# Example
c = [3, 7, 1, 4, 8, 22, 15, 18]
print(merge_sort2(c))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
