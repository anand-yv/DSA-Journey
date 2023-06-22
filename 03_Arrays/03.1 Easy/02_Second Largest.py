

class Solution:

    # brute force
    """
    def print2largest(self, arr, n):
        # code here
        arr.sort()
        largest = arr[n-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < largest:
                return arr[i]
        return -1
    """
    #  O(n log n) - O(1)

    # Better
    """
    def print2largest(self, arr, n):
        # code here
        largest = arr[0]
        for i in range(1, len(arr)):
            if largest < arr[i]:
                largest = arr[i]
        slargest = -1

        for i in range(len(arr)):
            if largest != arr[i] and slargest < arr[i]:
                slargest = arr[i]
        return slargest
    """
    # O(2N) - O(1)

    # Optimal Approach
    def print2largest(self, arr, n):
        # code here
        largest = arr[0]
        slargest = -1
        for i in range(1, len(arr)):
            if largest < arr[i]:
                slargest, largest = largest, arr[i]
            elif largest > arr[i] and slargest < arr[i]:
                slargest = arr[i]
        return slargest
    # O(n) - O(1)
