def binary_search(arr, target, start, end):
    while(start <= end):
        mid = (start+end)//2
        if(arr[mid] == target): # 값을 찾음
            return mid
        elif(arr[mid] > target): # 왼쪽 탐색
            end = mid -1
        else : # 오른쪽 탐색 
            start = mid +1
    
    return None # 값을 못찾았을 경우 None Return함