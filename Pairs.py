# QUESTION DESCRIPTION

# Given an array of integers and a target value, determine the number of pairs of array elements that have a
# difference equal to the target value.

# LET'S SOLVE IT

# Of course, there is the naive way to solve this problem. Here it is:

# def pairs(k, arr):

#     n = len(arr)
#     check = 0
#     for idx, a in enumerate(arr):
#         for b in arr[idx + 1:]:
#             if abs(a - b) == k:
#                 check += 1
#     return check

# Unfortunately, it is too naive for HackerRank. For some of the tests the program exceed the time limit of 10 secs.

# The code must be optimized. It can actually be linear:

def pairs(k, arr):

    n = len(arr)
    
    # Let us define a set whose elements are the entries of the array
    diff = set(arr)
    
    check = 0
    
    # To check if a-b = k, with a and b elements of arr, is equivalent to check if b = a-k is in the set diff just defined.
    # The implementation of sets as hash tables guarantees lookup/insert/delete in O(1) average. 
	
    for a in arr:
        if a-k in diff:
            check +=1

    return check



