def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    start = 0
    end = distance
    
    # mid는 바위간의 거리
    # mid를 늘리면 n의 개수가 감소
    # mid를 줄이면 n의 개수가 증가
    while end >= start:
        mid = (start + end) // 2
        current = 0
        cnt = 0
        min_distance = float('inf')
        for r in rocks:
           diff = r - current
           # mid값보다 큰 값은 카운팅한다. 가장 작은 거리중 최대값을 구해야하니
           # 가장 작은 거리값을 구하기위해서 큰 값들을 바위에서 제외시킨다.
           if diff >= mid:
               # 가장 짧은 거리 계산
               min_distance = min(diff, min_distance)
               current = r
           else:    
               # 지워진 바위 개수 카운팅
               cnt += 1
               
        if cnt > n:
            end = mid - 1
        else:
            # n보다 작거나 같을경우 min_distance를 갱신
            answer = min_distance
            start = mid + 1
            
    return answer