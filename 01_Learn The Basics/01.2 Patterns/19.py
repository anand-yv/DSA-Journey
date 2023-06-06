"""

* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * * 
* * * *     * * * *
* * * * * * * * * *

"""


print()
n = int(input("Enter the number : "))
print()

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(2*(n-1-i)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
