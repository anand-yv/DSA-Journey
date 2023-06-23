

# Finding Maximum Consecutives number of One's
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        anso = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if anso < count:
                anso = count
        return anso
# O(n) - O(1)