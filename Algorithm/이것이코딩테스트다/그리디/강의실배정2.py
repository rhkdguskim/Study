import heapq

def minimum_classrooms(n, schedule):
    schedule.sort(key=lambda x: x[0])  # 시작 시간(Si)을 기준으로 오름차순 정렬
    classrooms = []  # 강의실 리스트
    heapq.heappush(classrooms, schedule[0][1])  # 첫 번째 수업의 종료 시간을 최소 힙에 추가

    for i in range(1, n):
        start, end = schedule[i]
        if classrooms[0] <= start:  # 가장 빠른 종료 시간과 현재 수업의 시작 시간을 비교하여 겹치지 않으면
            heapq.heappop(classrooms)  # 해당 강의실을 사용할 수 있으므로 종료 시간을 갱신
        heapq.heappush(classrooms, end)  # 새로운 강의실을 생성하거나 기존 강의실에 현재 수업을 배정

    return len(classrooms)  # 사용된 강의실의 개수 반환


# 입력 예시
n = int(input())
schedule = []
for _ in range(n):
    s, t = map(int, input().split())
    schedule.append((s, t))

result = minimum_classrooms(n, schedule)
print(result)