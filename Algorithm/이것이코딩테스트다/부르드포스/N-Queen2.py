N = int(input())
count = 0

def is_valid(queens, row, col):
    for i in range(row):
        prev_row, prev_col = queens[i]
        if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def place_queen(queens, row):
    global count

    if row == N:  # 퀸을 모두 배치한 경우
        count += 1
        return

    for col in range(N):
        if is_valid(queens, row, col):
            queens.append((row, col))
            place_queen(queens, row + 1)
            queens.pop()

queens = []  # 퀸들의 위치를 저장하는 리스트

place_queen(queens, 0)
print(count)