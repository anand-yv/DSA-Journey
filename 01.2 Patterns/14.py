"""

A
A B
A B C
A B C D
A B C D E

"""


print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
print()