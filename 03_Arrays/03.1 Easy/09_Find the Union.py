
# Finding the Union - With Distinct Elements

class Solution:

    # Function to return a list containing the union of the two arrays.

    # Brute Force
    """
    def findUnion(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        seto = set(())
        for i in a:
            seto.add(i)
        for j in b:
            seto.add(j)
        return sorted(seto)
    """
    # O(3n log n) - O(n)

    # Optimal Approach
    def findUnion(self, a, b, n, m):
        res = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] < b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        while i < n:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        while j < m:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        return res
    # O(n1+n2) - O(n1+n2)
