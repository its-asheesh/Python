def checkFirstSetBit(n):
    ans=1
    
    while(n%2!=1):
        n=n>>1
        ans+=1
    return ans
def main():
    n=9
    ans = checkFirstSetBit(n)
    print(ans)
main()


