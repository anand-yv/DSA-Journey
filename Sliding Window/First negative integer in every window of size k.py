
# First negative integer in every window of size k
"""
Given an array A[] of size N and a positive integer K,
find the first negative integer for each and every window(contiguous subarray) of size K.
"""

def printFirstNegativeInteger( A, N, K):
    # code here
    res = []
    i,j = 0, 0
    temp = []
    while j < N:
        if A[j] < 0 :
            temp.append(A[j])
        if j - i + 1 < K: j+= 1
        elif j - i + 1 == K:
            if temp == []: res.append(0)
            else:
                res.append(temp[0])
                if A[i] == temp[0]:
                    temp.remove(temp[0])
            i += 1
            j += 1
    return res
