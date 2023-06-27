
# Longest Subarray with sum K | [Postives and Negatives]

# Brute Refer from Previous 13th

# Optimal Approach
class Soultion:
    def lenOfLongSubarr(self, nums, n, k):
        # Complete the function0
        maxlen = 0
        sumo = 0
        preSumMap = {}
        for i in range(len(nums)):
            sumo += nums[i]

            if sumo == k:
                maxlen = max(maxlen, i+1)

            rem = sumo - k
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxlen = max(maxlen, length)

            if sumo not in preSumMap:
                preSumMap[sumo] = i

        return maxlen
    # O(n) - O(n)
