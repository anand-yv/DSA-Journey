
# Find Missing Numbers

# Brute Force Approach - Compare it with each Element
# O(n^2) - O(1)

# Better Approach  - Use Hash Map - To store occurences 1 to N
# O(2n) - O(n)

# Optimal Approach - 1
def missingNumber(A, N):
    # Your code goes here
    sumo = (N*(N+1))//2
    for i in A:
        sumo -= i
    return sumo
# O(n) - O(1)

# Optimal Apprach - Using XOR
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor = 0
        i = 0
        for i in range(len(nums)):
            xor = xor ^ nums[i] ^ (i)
        return xor ^ (i+1)
# O(n) - O(1)


