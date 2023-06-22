
# Largest Element in Array
"""
Given an array A[] of size n. 
The task is to find the largest element in it.
"""


def largest(arr, n):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max

# O(n) - O(1)

