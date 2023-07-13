

def rearrangeArray(self, nums: list[int]) -> list[int]:
    pos, neg = [], []
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    res = []
    for i in range(0, len(nums), 2):
        nums[i] = pos[i//2]
    for i in range(1, len(nums), 2):
        nums[i] = neg[i//2]
    return nums
