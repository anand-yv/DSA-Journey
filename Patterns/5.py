"""

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
    for j in range(n,i,-1):
        print("*",end=" ")
    print()
print()