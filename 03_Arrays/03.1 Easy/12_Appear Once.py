

# Find the number that appears once, and the other numbers twice

# Brute Force - Compare with each element
# O(n^2) - O(n)

# Better - Use hash Set

# Optimal - Use Hashmap
# O(n/2 + 2) - O(n/2 + 1)

# Optimal
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
# O(n) - O(1)