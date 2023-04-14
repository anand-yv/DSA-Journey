#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        gcdo = self.gcd(A,B)
        lcmo = (A*B)//gcdo
        return [lcmo,gcdo]
        
    
    def gcd (self,A,B):
        if B==0: return A
        return self.gcd(B,A%B)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends