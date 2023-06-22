
# Left Rotate an array by on place

# Brute Force
class Solution:
    def leftRotate(self, arr, k, n):
        # Your code goes here
        k = k % n
        for i in range(k):
            temp = arr[0]
            for j in range(1, n):
                arr[j-1] = arr[j]
            arr[n-1] = temp
        return
    # O(n*k) + O(1)