arr = [11,12,13,14,15,1,2,3,4,5,6]

def SelectionSort(arr) :
    n = len(arr)
    for i in range(0,n) :
        idx = i
        for j in range(i+1, n):
            if arr[idx] > arr[j] :
                idx = j
                
                
        arr[i], arr[idx] = arr[idx], arr[i]
        
        
SelectionSort(arr)

print(arr)