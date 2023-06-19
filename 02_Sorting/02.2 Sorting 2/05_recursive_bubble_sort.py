
class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        # code here
        if n == 1:
            return
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        self.bubbleSort(arr, n-1)


obj = Solution()
arr = [2,6,8,2,3,6,7,5,85]
print("\nBefore Sorting : ",arr)
obj.bubbleSort(arr,len(arr))
print("After Sorting  : ",arr)