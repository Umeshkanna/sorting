def quick_sort(arr):
    n=len(arr)
    if(n<=1):
        return arr
    
    pivot=arr[-1]

    left=[x for x in arr[:-1] if x<= pivot]
    right=[x for x in arr[:-1] if x> pivot]
    
    return quick_sort(left)+[pivot]+quick_sort(right)


arr=list(map(int,input().split()))
sorte=(quick_sort(arr))
print(sorte)


def quick(arr,low,high):
    if(low<high):

        pivotind=partition(arr,low,high)

        quick(arr,low,pivotind-1)
        quick(arr,pivotind+1,high)


def partition(arr,low,high):
    i=low-1

    for  j in range(low,high):
        if(arr[j]<=high):
            i +=1
            arr[j], arr[i]=arr[i],  arr[j]


    arr[i+1], arr[high]= arr[high], arr[i+1]

    return i+1


arr=list(map(int,input().split()))
quick(arr,0,len(arr)-1)
print(arr)