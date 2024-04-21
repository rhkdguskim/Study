

# routes를 end시점으로부터 오름차순으로 정렬한다.
# routes의 마지막에 카메라를 설치한다.
# 1. 설치한위치가 다음 리터레이션의 routes에 범위안에 있다면 무시
# 2. 설치위치가 다음 리터레이션에서 routes의 범위안에 없다면 마지막에 카메라를 설치한다.

def solution(routes):
    routes.sort(key=lambda x:(x[1]))
    answer = 0

    prev_cam = -30001
    for s, e in routes:
        if s <= prev_cam:
            continue

        prev_cam = e
        answer += 1

    return answer