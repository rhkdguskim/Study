import sys
N = int(sys.stdin.readline().rstrip())
stordata = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
userdata = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, target, start ,end):
    result = False
    if(start > end):
        return False
    
    mid = (start+end)//2
    
    if(arr[mid] == target):
        return True
    elif(arr[mid] > target):
        result = binary_search(arr, target, start, mid -1)
    else :
        result = binary_search(arr, target, mid+1, end)
    
    return result

for i in range(M):
    print(binary_search(stordata, userdata[i], 0, N-1))