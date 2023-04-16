"""

A
B B
C C C
D D D D
E E E E E

"""

print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()
print()