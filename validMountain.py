

def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 1
    while i <len(arr) and arr[i] > arr[i-1]:
        i+=1

    if i == 1 or i == len(arr):
        return False 

    while i < len(arr) and arr[i] < arr[i-1]:
        i+=1

    return i == len(arr)


print(validMountainArray([1,2,5,2,1]))
