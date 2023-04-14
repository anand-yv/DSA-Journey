# Given a number N. Count the number of digits in N which evenly divides N.
class Solution:
    def evenlyDivides (self, N):
        # code here
        temp,count = N,0
        while N!=0:
            rem = N%10
            if rem != 0 and temp%rem == 0: count += 1
            N //= 10
        return count

#{  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       
        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends