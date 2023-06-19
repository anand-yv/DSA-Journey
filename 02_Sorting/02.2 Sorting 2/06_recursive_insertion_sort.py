
class Solution:
    def insertionSort(self, alist, index, n):
        # code here
        if index == n:
            return
        j = index
        while j > 0 and alist[j] < alist[j-1]:
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1
        self.insertionSort(alist, index+1, n)

obj = Solution()
arr = [2,6,8,2,3,6,7,5,85]
print("\nBefore Sorting : ",arr)
obj.insertionSort(arr,0,len(arr))
print("After Sorting  : ",arr)