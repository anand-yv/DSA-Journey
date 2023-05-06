# ROTATE ARRAY
"""
Given an array with N elements, the task is to rotate the array to the left by K steps,
where K is non-negative.
"""


# Using Temp Array (Slicing Concept)
"""
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
arr = arr[k:] + arr[:k]
for i in range(len(arr)): print(arr[i],end=" ")
"""

# Brute Force Approach (Rotate one by one)
"""
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
for i in range(k):
    temp = arr[0]
    arr = arr[1:]
    arr.append(temp)
for i in range(len(arr)): print(arr[i],end=" ")
"""

# Juggling Algorithm (Extension of Brute Force)
"""
def g_c_d(a,b):
    if b == 0:
        return a
    return g_c_d(b,a%b)

#Your code goes here.
n = int(input())
arr = list(map(int,input().split()))
n = len(arr)
d = int(input())
d = d%n
gcd = g_c_d(n,d)

for i in range(gcd):
    temp = arr[i]
    j = i
    while 1:
        k = j + d
        if k >= n:
            k = k - n
        if k == i:
            break
        arr[j] = arr[k]
        j = k
    arr[j] = temp

for i in arr:
    print(i,end=" ")

"""
