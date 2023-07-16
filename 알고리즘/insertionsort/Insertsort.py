arr = [5,6,7,8,9,0,1,2,3,4]

def InsertSort(arr) :
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1 # -1 만큼만 비교하면 됨
        while j >= 0 and arr[j] > key : # 탐색범위 조건 && Key가 배열보다 작으면 배열을 하나씩 뒤로 밈 key가 앞으로 가야하기 때문
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr

def InsertSort2(arr) :
    n = len(arr)
    for i in range (1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]: # 한칸씩 왼쪽으로 이동
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else :
                break
            
            
def quick_sort(arr, start , end) :
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # pivot을 첫번째 원소로 설정
    left = start +1
    right = end
    
    while left <= right :
        
        while left <= end and arr[left] <= arr[pivot]: # 피벗보다 큰 데이터를 찾을때까지 반복
            left += 1
        
        while right > start and arr[right] >= arr[pivot] : # 피벗보다 작은 데이터를 찾으면
            right -= 1
            
        if left >= right : # 엇갈림
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else :
            arr[right] , arr[left] = arr[left], arr[right]
            
        quick_sort(arr, start, right -1)
        quick_sort(arr, right + 1, end)
        


InsertSort2(arr)
print(arr)