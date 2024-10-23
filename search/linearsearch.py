pos=-1

def linearsearch(arr,n):


    for i in range(len(arr)):
        if(arr[i]==n):
            return i
    return -1


arr=[1,2,3,4,8]
n=8
print(linearsearch(arr,n))