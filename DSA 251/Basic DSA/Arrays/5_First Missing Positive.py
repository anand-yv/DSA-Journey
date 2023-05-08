# FIRST MISSING POSITIVE
"""
You are given an array 'ARR' of integers of length N. Your task is to find the first missing
positive integer in linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can have negative numbers as well.
For example, the input [3, 4, -1, 1] should give output 2 because it is the smallest positive
number that is missing in the input array.
"""

# SORTING AND TRAVESRSAL APPROACH
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        check = 1
        i = 0
        while i < len(nums):
            if check != nums[i]:
                if nums[i] > 0:
                    return check
                else:
                    i += 1
                    continue
            check += 1
            i += 1
        return check
"""
# O(nlog(n)) - O(n)


# INDEX MAPPING
# """
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            element = nums[i]
            chair = element - 1
            if(chair >= 0 and chair < n):
                if nums[chair] !=  element:
                    nums[chair], nums[i] = nums[i],nums[chair]
                else:
                    i += 1
            else:
                i += 1
            
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
            
# """

