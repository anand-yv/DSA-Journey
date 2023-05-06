
# SECOND LARGEST ELEMENT
"""
You have been given an array/list 'ARR' of integers. Your task is to find the second largest
element present in the 'ARR'.
"""


def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    listo = sequenceOfNumbers
    listo.sort()
    for i in range(len(listo)-1, -1, -1):
        if listo[i] != listo[i-1]:
            return listo[i-1]
    return -1

# Taking input using fast I/O.


def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().split()))

    return sequenceOfNumbers, n


# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
