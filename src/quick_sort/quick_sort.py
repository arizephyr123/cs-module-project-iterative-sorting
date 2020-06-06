# helper fn to partition L, pivot, R
def partitioner(arr):
    left = []
    right = []
    pivot = arr[0]

    # iterate over the arr
    ## if less than 
    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        if num > pivot:
            right.append(num)
    return left, right, pivot


def quick_sort(arr):
    if len(arr) == 0:
        return arr

    # partition here into left, pivot, right
    #divide
    left, right, pivot = partitioner(arr)

    # and conquer!
    return quick_sort(left) + pivot+ quick_sort(right)
