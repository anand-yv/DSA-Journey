print()
n = int(input("Enter the number : "))
print()
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        right = (2*n-2)-j
        down = (2*n-2)-i
        print(n-min(min(top, down), min(left, right)), end=" ")
    print()
print()
