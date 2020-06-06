def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found



# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # arr empty

    # index of high and low
    low = 0
    high = len(arr) -1

    while low <= high:
        # go to the middle
        middle = (low + high) //2
        #print()

    # ask if the middle is higher or lower than or greater than our target
    ## if less, eliminate the right hand side

        if target < arr[middle]:
            high = middle - 1

        elif target > arr[middle]:
            low = middle + 1

        else:
            return middle

    return -1  # not found
    