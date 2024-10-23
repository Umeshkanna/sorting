arr=[45,78,90,67,100,1045,9003]
n=len(arr)


for i in range(n):
    minind=i
    for j in range(i+1,n-1):
        if(arr[j]<arr[minind]):
            minind=j
    arr[minind],arr[i]=arr[i],arr[minind]

print(arr)