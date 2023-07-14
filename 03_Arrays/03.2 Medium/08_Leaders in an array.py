

# Leaders in an array problem.
# OPTIMAL APPROACH
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        res = []
        maxi = -1
        res.append(maxi)
        for i in range(len(arr)-1, 0, -1):
            maxi = max(arr[i], maxi)
            res.append(maxi)
        return reversed(res)
# O(n) - O(n)
