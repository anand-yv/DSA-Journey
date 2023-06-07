

# Check if String is palindrome or not

class Solution:
    def isPalindrome(self, S: str):
        # code here
        si, i = len(S), 0
        while i < si//2:
            if S[i] != S[si-i-1]:
                return False
            i += 1
        return True

    def recursion_isPalindrome(self, S: str, i: int, n: int):
        if i >= n//2:
            return True
        if S[i] != S[n-i-1]:
            return False
        return self.recursion_isPalindrome(S, i+1, n)


stro1 = "anand"
obj = Solution()
print("Normal : ",obj.isPalindrome(stro1))
print("Recursion : ",obj.recursion_isPalindrome(stro1,0,len(stro1)))

stro2 = "kayak"
print("Normal : ",obj.isPalindrome(stro2))
print("Recursion : ",obj.recursion_isPalindrome(stro2,0,len(stro2)))
