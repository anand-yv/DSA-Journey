
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex-1)
            self.quickSort(arr, pIndex+1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while arr[i] <= pivot and i <= high-1:
                i += 1
            while arr[j] > pivot and j >= low+1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j


obj = Solution()
arr = [2, 6, 8, 2, 3, 6, 7, 5, 85, 23, 6, 3, 4, 8, 5, 3, 6, 8, 555]
print("\nBefore Sorting : ", arr)
obj.quickSort(arr, 0, len(arr)-1)
print("After Sorting :  ", arr)
