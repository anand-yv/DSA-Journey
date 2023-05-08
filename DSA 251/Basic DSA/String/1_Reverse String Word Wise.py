
# REVERSE STRING WORD
"""
Reverse the given string word-wise. The last word in the given string should come at 1st
place, the last-second word at 2nd place, and so on. Individual words should remain as it
is.
"""

# USING SPIT AND STRIP FUNCTION
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        listo = s.split()
        print(listo)
        ans = ""
        for i in range(len(listo)-1,-1,-1):
            ans += listo[i] + " "
        return ans.strip()
"""
# O(n) - O(n) 

# Tow Pointer Approach 
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        left = 0
        n = len(s)
        while left < n:
            while left < n and s[left] == " ": # skip any leading spaces
                left += 1
            if left >= n: # if the left pointer reaches the end, break out of the loop
                break
            right = left + 1
            while right < n and s[right] != " ": # loop through the input string until the 
            # right pointer reaches the end or a space character
                right += 1
            sub_string = s[left:right]
            if len(ans) == 0:
                ans = sub_string
            else:
                ans = sub_string + " " + ans
            left = right + 1
        return ans
# O(n) - O(n) 
