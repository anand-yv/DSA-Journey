

# Print he last number of Fibonaccis Series
# 0 1 1 2 3 5 8 13 ...................

class Solution:
    def recursion_fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)

    def fib(self, n: int) -> int:
        anso = 0
        nexto = 1
        for i in range(n):
            temp = nexto
            nexto += anso
            anso = temp
        return anso


obj = Solution()
print("Recursion : ", obj.recursion_fib(5))
print("Normal : ", obj.fib(5))
