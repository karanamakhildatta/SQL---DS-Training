def sum_of_array(arr):
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
        if num == target:
            count = count + 1
    return count
def count_perfect_squares(arr):
    '''
    Find count of perfect squares in array
    '''
    count = 0
    for num in arr:
        if num**0.5 == int(num**0.5):
            count += 1
    return count

def find_total_of_perfect_squares(arr):
    '''
    Find total of perfect squares in array
    '''
    total = 0
    for num in arr:
        if num**0.5 == int(num**0.5):
            total += num
    return total

def find_average(arr):
    '''
    Calculate the average of all elements in the array
    '''
    total = sum_of_array(arr)
    number_of_elements = len(arr)
    average = total / number_of_elements
    return average

# find count even numbers in array

def count_even_numbers(arr):
    '''
    Find count of even numbers in array
    '''
    # even_number = number/2 => reminder == 0
    # % => it gives reminder
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

def count_odd_numbers(arr):
    pass
def find_total_of_odd_numbers(arr):
    pass
def find_total_of_even_numbers(arr):
    pass

def reverse_array(arr):
    '''
    Reverse the array
    '''
    left  = 0
    right = len(arr) - 1
    while left < right:
        arr[left],arr[right] = arr[right], arr[left]
        left+=1
        rigth-=1

