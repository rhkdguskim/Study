def binary_search(arr, target, start , end):
    if (start > end):
        return None

    mid = (start + end) // 2
    
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target) : # 중간점의 값이 타겟보다 클경우 타겟이 작으므로 작은 값에서 이진탐색실시
        binary_search(arr, target, start, mid -1)
    elif(arr[mid] < target) : # 중간점의 값이 타겟보다 작을 경우 타켓이 더 큼으로 큰 값에서 이진탐색실시
        binary_search(arr, target, mid+1, end)
