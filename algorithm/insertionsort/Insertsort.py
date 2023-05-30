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
        
                

InsertSort(arr)
print(arr)