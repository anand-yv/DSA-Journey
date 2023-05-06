# EQUILIBRIUM INDEX
"""
You are given an array Arr consisting of N integers. You need to find the equilibrium index
of the array.
An index is considered as an equilibrium index if the sum of elements of the array to the
left of that index is equal to the sum of elements to the right of it.
"""

# NAIVE APPROACH

"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            suml,sumr = 0,0
            for j in range(i):
                suml += nums[j]
            for j in range(i+1,len(nums)):
                sumr += nums[j]
            if suml == sumr:
                return i
        return -1
"""
# O(n^2) - O(1)


# ARRAY SUM 
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumr = sum(nums)
        suml = 0 
        for i in range(len(nums)):
            sumr -= nums[i]
            if suml == sumr:
                return i
            suml += nums[i]
        return -1
"""
# O(n) - o(1)