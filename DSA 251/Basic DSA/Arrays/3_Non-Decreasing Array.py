
# NON-DECREASING ARRAY
"""
You have been given an integer array list arr of size n write a solution to
check if it could become non decreasing by modifying at most 1 element
"""
# Greedy Approach


def isPossible(arr, n):
    # Write your code here.
    changed = False
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        if changed:
            return False
        if i == 0 or arr[i+1] >= arr[i-1]:
            arr[i] = arr[i+1]
        else:
            arr[i+1] = arr[i]
        changed = True
    return True
