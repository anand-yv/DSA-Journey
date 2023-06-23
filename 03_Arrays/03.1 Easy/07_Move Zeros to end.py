
# Move Zeros to end

class Solution:

    # Brute Force - Using Extra Array
    """
    def moveZeroes(self, nums: list[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp),len(nums)):
            nums[i] = 0
    """
    # O(2n) - O(n)

    # Optimal Approach
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[i] != 0:
                i += 1
    # O(n) - O(1)
