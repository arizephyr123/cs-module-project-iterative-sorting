# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # need to look ahead without going out of bounds
    # because last element will be sorted
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # inner loop goes all the way to end
        for j in range(cur_index + 1, len(arr)):
            # print("i:",i,"j:", j,"====", arr) 
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        
        # TO-DO: swap
        # Your code here
        #
        # temp = arr[i]
        # arr[cur_index] = arr[smallest_index]
        # arr[smallest_index] = temp
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
'''
def counting_sort(arr, maximum=None):
    counts = [0] * (maximum + 1)
    
    for val in arr:
        counts[val] += 1

    for i in range(0, range(counts)):
        while counts[i] > 0:
            arr[j] = i
            j+=1
            counts[i] -= 1



    return arr

test_arr = [4,3,2,1]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]

# selection_sort(arr1)
# selection_sort(arr2)
# selection_sort(arr3)
# selection_sort(test_arr)
bubble_sort(test_arr)
