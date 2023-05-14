
# NEXT SMALLEST PALLINDROME
"""
You are given a number 'N' in the form of a string 'S', your task is to find the smallest
number strictly greater than the given number 'N' which is a palindrome.
"""


def is_pallindrome(a):
    return a == a[::-1]

def add_1(a):
    return str(int(a)+1)

def compare(x,y):
    for i,j in zip(x,y):
        if int(i) > int(j): return 1
        elif int(i) < int(j): return -1
        else: continue
    return 0

def handle_odd(a):
    n = len(a)
    left = a[:n//2]
    mid = a[n//2]
    right = a[n//2+1:]
    if compare(left[::-1],right) == 1:
        return left + mid + left[::-1]
    else:
        left = left + mid
        left = add_1(left)
        return left+left[::-1][1:]

def handle_even(a):
    n  = len(a)
    left = a[:n//2]
    right = a[n//2:]
    if compare(left[::-1],right) == 1:
        return left + left[::-1]
    else:
        left = add_1(left)
        return left + left[::-1]

def nextLargestPalindrome(a):
    if is_pallindrome(a): a = add_1(a)

    if len(a) % 2 != 0:
        return handle_odd(a)
    else:
        return handle_even(a)


s = input("Enter the number: ")
print(nextLargestPalindrome(s))