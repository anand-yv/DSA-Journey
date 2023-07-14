

# NEXT PERMUTTAION - Optimal Approach
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1 :
            nums.sort()
            return
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[index]:
                nums[i],nums[index] = nums[index], nums[i]
                break
        
        nums[index+1:] = reversed(nums[index+1:])
# O(3n) - O(1)



    
        