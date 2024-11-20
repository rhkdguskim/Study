import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

    # 같은 중심
    if x1 == x2 and y1 == y2:
        if r1 == r2:  # 두 원이 완전히 겹침
            print(-1)
        else:  # 같은 중심이지만 반지름이 다름
            print(0)
    else:
        # 교점 개수 계산
        if distance > r1 + r2:  # 두 원이 서로 떨어져 있음
            print(0)
        elif distance == r1 + r2:  # 두 원이 외접
            print(1)
        elif abs(r1 - r2) < distance < r1 + r2:  # 두 원이 서로 겹침
            print(2)
        elif distance == abs(r1 - r2):  # 두 원이 내접
            print(1)
        else:  # 한 원이 다른 원 안에 있음
            print(0)