
# Kadane’s Algorithm : Maximum Subarray Sum in an Array
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        sumo = 0
        for i in range(len(nums)):
            sumo += nums[i]
            if sumo > ans:
                ans = sumo
            if sumo < 0:
                sumo = 0
        return ans
# O(n) - O(1)
