
# Optimal Approach
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        elem = None
        for i in nums:
            if count == 0:
                count += 1
                elem = i
            elif elem == i:
                count += 1
            else:
                count -= 1
        return elem
# O(n) - O(1)