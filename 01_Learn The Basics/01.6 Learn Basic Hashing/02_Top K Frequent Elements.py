
# Top K Frequent Elements
"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicto = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            dicto[i] = 1 + dicto.get(i,0)
        for i,j in dicto.items():
            freq[j].append(i)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k: return res
        