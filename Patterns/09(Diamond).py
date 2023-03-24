"""

    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

"""


print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()
    
print()