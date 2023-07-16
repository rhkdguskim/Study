# 손님이 요청한 길이가 M일때 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성하세요.
arr = [15, 16, 17, 18, 19, 20, 21 , 22]
m = 10
start = 0
end = max(arr)

# 이진 탐색을 위하여 시작값과 끝 값을 지정한다.
while (start <= end) :
    total = 0 # m만큼의 떡을 억기위한 누적기
    mid = (start + end) // 2 # 중간값 설정
    for x in arr: # 누적값을 계산한다
            if x > mid:
                total += x - mid
                
    if total < m : # 누적된 값이 Total이 작을경우 최대값의 범위는 더 작은곳에 있다. (왼쪽)
        end = mid -1
    else :
        result = mid # 누적된 값이 Total보다 클 경우 최대값의 범위는 더 큰곳에 있다. (오른쪽)
        start = mid + 1
        
print(result)