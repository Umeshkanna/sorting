def bubblesort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1): 
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr

arr=[1,2,3,5,0]
print(bubblesort(arr))