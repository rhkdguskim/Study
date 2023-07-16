arr = [1,2,5,6,7,8,9,10]

def BubbleSort(arr) :
    n = len(arr)
    for i in range(n - 1) :
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                Swap(arr[j], arr[j+1])
        
BubbleSort(arr)

def Swap(a,b):
    temp = a
    a = b
    b = temp

print(arr)