"""

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""


print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-1-i):
        print("*",end=" ")
    print()
print()