# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # need to look ahead without going out of bounds
    # because last element will be sorted in inner loop
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # inner loop goes from arr[1] to arr[-1]
        for j in range(cur_index + 1, len(arr)):
            # print("i:",i,"j:", j,"====", arr) 
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        
        # swap for smallest for lower val
        #
        # temp = arr[i]
        # arr[cur_index] = arr[smallest_index]
        # arr[smallest_index] = temp
        # 
        # cleaner as:

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
       
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # start with True to initiate
    made_swap = True

    while made_swap:
        made_swap = False
        for i in range(len(arr) - 1):
            j = i + 1
            # print("i:", i, "j:", j, "made_swap:", made_swap, "====", arr)
        
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                made_swap = True
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?

time complexity is O(n)
'''
def count_sort(arr, maximum=-1):
    # if empty, return 
    if len(arr) == 0:
        return arr

    # if max is not given then change default to highest value in max array
    if maximum == -1:
        # find max val in arr
        maximum = max(arr)  
    
    # holding space for all possible values from 0-maximum
    counts = [0] * (maximum + 1) # [0, 1, 2, 3 ... max]

    # looping through arr
    for val in arr:
        # sending error for negative nums
        if val < 0:
            return 'Error, negative numbers not allowed in Count Sort'

        # incrementing idex of counts for each value 
        # ex: counts[4] += 1   
        # counts index is same as value
        # [0, 0, 0, 0, 1, 0, ... max]
        counts[val] += 1

    # keeps track of the index of return arr
    j=0
    # loop through counts array
    for i in range(len(counts)):
        # while value has at least one count in original arr param
        while counts[i] > 0:
            # remember, counts[i] is number of 'i' being counted
            # counts[4] = 1 --> there was one 4 in the array
            # arr[j]
            arr[j] = i
            # iterate to next index in arr
            j+=1
            # decrement that val count from counts arr
            counts[i] -= 1

    return arr

test_arr = [4,3,2,1]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1,-2,  2, 3, 4, 5]

# selection_sort(arr1)
# selection_sort(arr2)
# selection_sort(arr3)
# selection_sort(test_arr)
# bubble_sort(test_arr)
print(count_sort(test_arr))
print(count_sort(arr1))
print(count_sort(arr2))
print(count_sort(arr3))
