import sys

input = sys.stdin.readline

X = int(input())

line = 1
up = 1
down = 1

while X > line:
    X -= line
    line += 1

    # 짝수일때 (부모감소, 자식증가)
    if line % 2 == 0:
        up = X
        down = line - X + 1
    # 홀수일때 (부모증가, 자식감소)
    else:
        down = X
        up = line - X + 1

print(up, '/', down, sep='')