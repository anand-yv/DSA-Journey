
# LeetCode: 921. Minimum Add to Make Parentheses Valid
"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. 
In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))"
or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""

# STACK Approach


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        arr = []
        for i in range(len(s)):
            if s[i] == "(":
                arr.append("(")
            elif s[i] == ")" and len(arr) > 0:
                arr.pop()
            elif s[i] == ")" and len(arr) <= 0:
                ans += 1
        return len(arr) + ans
# O(n) - O(n)


# Blanced Parantheses Approach
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        not_opened = not_closed = 0
        for i in s:
            if not_closed == 0 and i == ")":
                not_opened += 1
            else:
                if i == "(":
                    not_closed += 1
                else:
                    not_closed -= 1
        return not_opened+not_closed
# O(n) - O(1)
