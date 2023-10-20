import sys
input = sys.stdin.readline
s = []

for _ in range(3):
    s.append(list(map(int, input().split())))

def check(s):
    colsum = s[0][0] + s[1][0] + s[2][0]
    rowsum = sum(s[0])
    cross1 = s[0][0] + s[1][1] + s[2][2]
    cross2 = s[0][2] + s[1][1] + s[2][0]

    for i in range(3): # check raw and col
        if i != 0:
            if colsum != (s[0][i] + s[1][i] + s[2][i]):
                return False
            if rowsum != sum(s[i]):
                return False

    if cross1 == cross2:
        return True
    else:
        return False

def calculate(s1, s2):
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += abs(s1[i][j] - s2[i][j])

    return temp



ans = 90
def dfs(number):
    global ans
    if len(number) == 9:
        s2 = []
        s2.append(number[:3])
        s2.append(number[3:6])
        s2.append(number[6:9])
        if check(s2):
            ans = min(calculate(s, s2), ans)
        return

    for num in range(1, 10):
        if num not in number:
            number.append(num)
            dfs(number)
            number.pop()

dfs([])
print(ans)