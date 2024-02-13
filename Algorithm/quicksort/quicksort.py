# 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
    if start >= end : # 원소가 1개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    
    while(left <= right) :
        while(left <= end and array[left] <= array[pivot]) : # 좌측에서 피벗 값보다 큰 데이터를 찾는 idx 선형탐색
            left += 1
            
        while(right > start and array[right] >= array[pivot]) : #우측에서 피벗 값보다 작은 데이터를 찾는 idx 선형탐색
            right -=1
            
        if(left >right): # 서로 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right] , array[pivot] = array[pivot], array[right]
        else : # 엇 갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
            
        quick_sort(array, start, right -1)
        quick_sort(array, right+1, end)
        
quick_sort(array, 0, len(array) - 1)
print(array)            
            