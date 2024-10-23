def binarysearch(arr,n):
    l=0
    h=len(arr)-1

    mid=(l+h)//2

    if(arr[mid]==n):
        return mid
    else:
        if(arr[mid]<n):
            l=mid+1
        else:
            h=mid+1
    return -1

arr=[1,2,3,4,5]
arr=sorted(arr)
n=3
if(binarysearch(arr,n))!=-1:
    print("Yes")
else:
    print("No")

print(binarysearch(arr,n))

    