class Solution:
    def reverse(self, x: int) -> int:
        check = 0
        if x < 0:
            x = -1 * x
            check = 1
        ans = 0
        while x != 0:
            ans = ans*10 + x % 10
            x //= 10
        if (-2**31 > ans or 2**31 - 1 < ans):
            return 0
        return (ans if check == 0 else (-1*ans))

obj1 = Solution()
print(obj1.reverse(63))