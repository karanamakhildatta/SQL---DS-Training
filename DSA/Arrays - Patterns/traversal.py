def traversal(arr):
    #Method 1 : using for loop:
    for i in range(len(arr)):
        print(arr[i])
    #Method 2 : Going through element:
    for element in arr:
        print(element)
    # using enumerate
    # enumerate(a) provides both the index (i) and the element (name) during iteration.
    # example 1: [(0,1),(1,2),(index,value)]

    for index, value in enumerate(arr):
        print(f"Index is {index} and value is {value}")

# def count_occurrences(arr, target):
#     """
#     Simple O(n) approach - just count matches.
#     Use when array is NOT sorted or is very small.
#     """


traversal([1,2,3,4,5])