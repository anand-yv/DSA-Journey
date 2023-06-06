
# Using Recursion

class Solution:
    def sumOfNumbers_recursionFunction(self,n:int) -> int:
        if n == 1: return 1
        return (n + self.sumOfNumbers_recursionFunction(n-1))

    def sumOfNumbers_formula(self,n:int) -> int:
        return (n*(n+1))//2

N = int(input("Enter the number : "))
obj = Solution()
print("Recursion Function: ",obj.sumOfNumbers_recursionFunction(N))
print("Numbers Formula: ",obj.sumOfNumbers_formula(N))