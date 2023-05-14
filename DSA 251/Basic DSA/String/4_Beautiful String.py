
# Minimum Changes To Make Alternating Binary String
"""
You are given a string s consisting only of the characters '0' and '1'.
 In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""



# GENERATE AND COMPARE
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        gen1 = self.generate(n, True)
        diff1 = self.difference(s,gen1)
        
        gen2 = self.generate(n, False)
        diff2 = self.difference(s,gen2)

        return min(diff1,diff2)
    
    def generate(self,n: int, zero: bool) -> str:
        if n == 0: return ""
        ans = ""
        if zero:ans +=  "0"
        else: ans += "1"
        n -= 1
        while n!=0:
            ans += "0" if ans[len(ans)-1] == "1" else "1"
            n -= 1
        return ans
    
    def difference(self,orig: List, comp: List) -> int:
        ans = 0
        for i in range(len(orig)):
            if orig[i] != comp[i]: ans += 1
        return ans
# O(n) - O(n)


# GRREEDY APROACH
class Solution:
    def minOperations(self, s: str) -> int:
        ans1 = ans2= 0
        for i in range(len(s)):
            z=str(i%2)
            ans1+=s[i]!=z
            ans2+=s[i]==z
        return min(ans1,ans2)
# O(n) - O(1)

        
