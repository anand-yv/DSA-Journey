
# Left Rotate by one Place

# See Brute force approch on previous sum

# Optimal Approach
class Solution:
    def leftRotate(self, arr, n, k):
        # code here
        k = k % n
        temp = []
        for i in range(k):
            temp.append(arr[i])
        for i in range(k, n):
            arr[i-k] = arr[i]
        for i in range(n-k, n):
            arr[i] = temp[i-(n-k)]
    # O(n+k) - O(n)