"""

          A
        A B A
      A B C B A
    A B C D C B A
  A B C D E D C B A

"""

print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    for j in range(i,0,-1):
        print(chr(65+j-1),end=" ")
    print()
print()