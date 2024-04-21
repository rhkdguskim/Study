
def solution(citations):
    start = 0
    end = len(citations)
    answer = 0
    while end >= start:
        mid = (start + end) // 2

        cnt = 0
        for c in citations:
            if c >= mid:
                cnt += 1

        # n편 이상 발견되었다면 값을 h값을 늘려본다
        if cnt >= mid:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer