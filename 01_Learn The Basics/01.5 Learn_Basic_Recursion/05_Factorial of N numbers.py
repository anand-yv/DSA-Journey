
# Finding Factorial of Numbers

class Solution:
    def factorialRecursion(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.factorialRecursion(n-1)

    def factorial(self, n: int) -> int:
        f = 1
        for i in range(1,n+1):
            f *= i
        return f


N = int(input("Enter the number : "))
obj = Solution()
print("Recusrion : ",obj.factorialRecursion(N))
print("Normal : ",obj.factorial(N))
