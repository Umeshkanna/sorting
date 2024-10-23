def linearsearch(arr,n):

    for i in range(len(arr)):
        if arr[i]==n:
            return i
        
    return "No"


n=4
arr=[1,2,3,4,6,7]
print(linearsearch(arr,n))