import bisect

def minimum_classrooms(n, schedule):
    schedule.sort(key=lambda x: x[0])  # 시작 시간(Si)을 기준으로 오름차순 정렬
    classrooms = []  # 강의실 리스트

    for i in range(n):
        start, end = schedule[i]
        index = bisect.bisect_left(classrooms, start)  # 종료 시간이 start보다 크거나 같은 강의실 탐색
        if index != len(classrooms):  # 해당 강의실이 존재하면
            classrooms[index] = end  # 강의실의 종료 시간 갱신
        else:  # 해당 강의실이 존재하지 않으면
            classrooms.append(end)  # 새로운 강의실 생성

    return len(classrooms)  # 사용된 강의실의 개수 반환


# 입력 예시
n = int(input())
schedule = []
for _ in range(n):
    s, t = map(int, input().split())
    schedule.append((s, t))

result = minimum_classrooms(n, schedule)
print(result)