def binarySearch(arr,se):
    arr.sort()
    l=0
    r=len(arr)-1
    while(l<=r):
        mid = (l+r)//2
        if(arr[mid]==se):
            return "Element is present in the given array."
            
        if(arr[mid]>se):
            r=mid-1
        else:
            l=mid+1
    return "Element is not present in the given array."

def main():
    
    arr = [1,9,1,11,12,15,5]
    se = int(input("Enter element to be searched: "))
    print(binarySearch(arr,se))
main()
