def kthBitIsSetOrNot(n,k):
    x =(n>>(k-1))
    if((x&1)!=0):
        print("1")
    else:
        print("0")
kthBitIsSetOrNot(81,2)
