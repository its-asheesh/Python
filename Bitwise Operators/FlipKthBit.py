def flipBit(n,k):
    n = n^(1<<(k-1))
    print("Number after flipping the bit :",n)
def main():
    n = int(input("Enter the number : "))
    k = int(input("Enter the bit position to be flipped : "))
    flipBit(n,k)
main()
