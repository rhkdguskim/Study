import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().rstrip().split()))
def binary_search(arr, target, start, end):
    result = 0
    if(start > end):
        return 0
    
    mid = (start+end) // 2
    if(target == arr[mid]):
        return 1
    elif(target > arr[mid]):
        result = binary_search(arr, target, mid +1, end)
    else :
        result = binary_search(arr, target, start, mid -1)
        
    return result

for i in range(M):
    print(binary_search(arr, arr2[i], 0, len(arr) - 1))