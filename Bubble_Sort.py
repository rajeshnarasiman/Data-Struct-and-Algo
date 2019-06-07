def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapping = False
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapping = True
        if swapping == False:
            break
    print(arr)


#driver code
arr= [54,34,33,22,77,28,88,55,56,100]
bubblesort(arr)
