
class Solution:
    def insertionSort(self, alist, n):
        # code here
        for i in range(n):
            j = i
            while (j > 0) and (alist[j] < alist[j-1]):
                alist[j-1], alist[j] = alist[j], alist[j-1]
                j -= 1

obj = Solution()
arr = [4,5,63,23,21,1,6,3]
print("\nBefore Sorting : ",arr)
obj.insertionSort(arr,len(arr))
print("After Sorting  : ",arr)