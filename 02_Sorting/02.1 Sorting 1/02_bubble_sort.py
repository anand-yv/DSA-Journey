

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        # code here
        for i in range(n-1):
            count = 0
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    count = 1
            if count == 0: return


obj = Solution()
arr = [4,1,3,9,7,2,6,3,5]
print("\nBefore Sorting : ",arr)
obj.bubbleSort(arr,len(arr))
print("After Sorting  : ",arr)