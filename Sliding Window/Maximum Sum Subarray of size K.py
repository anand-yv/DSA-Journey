
# Max Sum Subarray of size K
"""
Given an array of integers Arr of size N and a number K.
Return the maximum sum of a subarray of size K.
"""
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        start, end = 0, 0
        ans,sumo = 0, 0
        while end < N:
            sumo = sumo + Arr[end]
            if end-start+1<K: end+=1
            elif end-start+1 == K:
                ans = max(ans,sumo)
                sumo -= Arr[start]
                start+=1
                end+=1
        return ans