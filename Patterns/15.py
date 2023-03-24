print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()
print()