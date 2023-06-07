
# Reverse an Array

class Solution:
    def recursion1(self, arr: list, start: int, end: int):
        if start >= end: return
        arr[start], arr[end] = arr[end], arr[start]
        self.recursion1(arr,start + 1,end-1)
    
    def recursion2(self,arr: list,i:int,n:int):
        if i >= n//2: return
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
        self.recursion2(arr,i+1,n)

arr1 = [1,2,3,4,5]

obj = Solution()
obj.recursion1(arr1,0,len(arr1)-1)
print("Recursion 1 : ",arr1)
obj.recursion2(arr1,0,len(arr1))
print("Recursion 2 : ",arr1)



