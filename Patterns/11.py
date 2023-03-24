print()
n = int(input("Enter the number : "))
print()
for i in range(n):
    count = 0
    if i % 2 == 0:
        count = 1
    for j in range(i+1):
        print(count, end=" ")
        count = 1 - count
    print()
print()