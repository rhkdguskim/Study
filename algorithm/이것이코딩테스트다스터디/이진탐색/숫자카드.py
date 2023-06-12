# https://www.acmicpc.net/problem/10816
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
    if(target == arr[mid]): # 해당 값을 찾았으면 총 개수를 구한다
        right = mid
        left = mid
        while( left >= 0 and target == arr[left]):
            result +=1
            left -= 1
        
        right += 1
        while(right < len(arr) and target == arr[right]):
            result +=1
            right += 1
        
        return result
    elif(target > arr[mid]):
        result = binary_search(arr, target, mid +1, end)
    else :
        result = binary_search(arr, target, start, mid -1)
        
    return result

data = dict()
for i in range(M):
    if arr2[i] in data: # 이미 값이 구해진 값이라면 탐색하지 않는다.
        print(data[arr2[i]], end=' ')
    else :
        data[arr2[i]] = binary_search(arr, arr2[i], 0, len(arr) - 1)
        print(data[arr2[i]], end=' ')