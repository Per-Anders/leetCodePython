def maxSum(arr,windowSize):
    arraySize = len(arr)
    if(arraySize <= windowSize):
        print("invalid operation")
        return -1
    
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum

    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i+windowSize]
        max_sum = max(window_sum, max_sum)
    
    return max_sum


print(maxSum([80,-50,90,100], 2))
