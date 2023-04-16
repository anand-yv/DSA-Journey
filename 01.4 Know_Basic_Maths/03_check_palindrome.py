class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0 or (x>0 and x%10 == 0): return False
        ans = 0
        while ans < x:
            ans = ans*10 + x%10
            x //= 10
        return True if (x == ans or x == ans//10) else False