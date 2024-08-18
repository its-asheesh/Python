def linearSearch(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return True
    return False

def main():
    target = int(input("Enter the Element to be Searched : "))
    arr = [1,2,3,4]
    print(linearSearch(arr,target))
main()
