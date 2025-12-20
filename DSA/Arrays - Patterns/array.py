def find_sum(arr):
    '''
    Calculate the sum of all elements in the array
    '''
    total = 0 # Initialize sum to 0
    for num in arr: # iterate through each element in the array
        total += num # add current element to total sum
    return total # return total sum

def find_max(arr):
    '''
    Find the maximum element in the array
    '''
    max = arr[0] # Assume first element is the maximum
    for num in arr: # iterate through each element in the array
        if num > max: # check if current element is greater than max
            max = num # Update max if current element is greater
    return max # return the maximum element found

def find_min(arr):
    '''
    Find the minimum element in the array
    '''
    min  = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min

def count_occurrences(arr, target):
    '''
    Count occurrences of target in the array
    '''
    count  = 0
    for num in arr:
        if num ==target:
            count = count + 1
    return count
