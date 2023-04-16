class Check:
    def prime_num(self,n):
        for i in range(2,n):
            if n%i == 0: return False
        return True

    def prime_num_optimized(self,n):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0: return False
        return True

if __name__ == "__main__":
    # without optimization
    det = Check()
    n = int(input("Enter the number you want to check : "))
    see = det.prime_num(n)
    if n > 1 and see: print(f"{n} is prime number")
    else: print(f"{n} is not a prime number")

    # with optimization
    det1 = Check()
    n = int(input("Enter the number you want to check : "))
    see = det1.prime_num_optimized(n)
    if n > 1 and see == True: print(f"{n} is prime number")
    else: print(f"{n} is not a prime number")

