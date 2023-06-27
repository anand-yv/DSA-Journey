

# Longest Subarray with given Sum K(Positives)

class Solution:
    # Brute Force Approach /  Better Approach
    """
    def lenOfLongSubarr (self, nums, n, k) : 
        #Complete the function0
        ans = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(i,len(nums)):
                temp += nums[j]
                if temp == k:
                    ans = max(ans,(j-i+1))
        return ans
    """
    # O(n^2) - O(1)

    # Optimal Approach
    def lenOfLongSubarr(self, nums, n, k):
        # Complete the function
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


    # BEST
    def longestSubarrayWithSumK(a: list[int], k: int) -> int:
    # Write your code here
        left,right= 0,0
        maxLen = 0
        sumo = a[0]
        while right < len(a):
            while left <= right and sumo > k:
                sumo -= a[left]
                left += 1

            if sumo == k:
                maxLen = max(maxLen, right - left + 1)
        
            right += 1
            if right < len(a):
                sumo += a[right]
        
        return maxLen
    # O(n) - O(1)
