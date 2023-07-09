

# Better Approach: Using Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        dicto = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dicto:
                return [dicto[rem],i]
            else:
                dicto[nums[i]] = i
# O(n) - O(n)