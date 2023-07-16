N = int(input())
count = 0

def is_valid(queens, row, col):
    for i in range(row):
        if queens[i] == col or queens[i] - col == i - row or queens[i] - col == row - i:
            return False
    return True

def place_queen(queens, row):
    global count

    if row == N:  # 퀸을 모두 배치한 경우
        count += 1
        return

    for col in range(N):
        if is_valid(queens, row, col):
            queens[row] = col
            place_queen(queens, row + 1)

queens = [0] * N  # 각 행에 배치된 퀸의 열 인덱스를 저장하는 리스트

place_queen(queens, 0)
print(count)