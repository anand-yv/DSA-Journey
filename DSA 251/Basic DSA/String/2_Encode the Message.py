
# ENCODE THE MESSAGE
"""
You have been given a text message. You have to return the Run-length Encoding of the
given message.
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to
represent repeated successive characters as the character and a single count. For
example, the string "aaaabbbccdaa" would be encoded as "a4b3c2d1a2".
"""

# LINEAR SCAN APPROACH
def encode(message):
    # Write your code here.
    count = 1
    ans = ""
    for i in range(len(message)):
        if i < len(message)-1 and message[i] == message[i+1]:
            count += 1
        elif i == len(message)-1:
            ans += message[i] + str(count)
        else:
            ans += message[i] + str(count)
            count = 1
    return ans
# O(n) - O(n)

# TWO POINTER APROACH
def encode(message):
    # Write your code here.
    left = 0
    right = 0
    ans = ""
    while left < len(message):
        while right < len(message) and message[left] == message[right]:
            right += 1
        ans += message[left] + str(right-left)
        left = right
    return ans
# O(n) - O(n)