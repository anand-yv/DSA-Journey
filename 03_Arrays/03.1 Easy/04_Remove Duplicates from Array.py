
# Remove Duplicates from Sorted Array

class Solution:

    # Optimal Approach
    def remove_duplicate(self, A, N):
        # code here
        i = 0
        for j in range(1, N):
            if A[i] != A[j]:
                A[i+1] = A[j]
                i += 1
        return i+1
    # O(n) - O(1)
