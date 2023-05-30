def soulution(n,k,arr, arr2) :
    for _ in range(k):
        arr[arr.index(min(arr))], arr2[arr2.index(max(arr2))] = arr2[arr2.index(max(arr2))], arr[arr.index(min(arr))]
    
    print(sum(arr))
    
soulution(5,3,[1,2,5,4,3],[5,5,6,6,5])