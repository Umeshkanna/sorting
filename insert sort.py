arr=list(map(int,input().split()))


    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        
    arr[j+1]=key
print(arr)
