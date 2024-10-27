import sys
input = sys.stdin.readline

N, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def multi_plex(matrix1, matrix2):
    n = len(matrix1)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            new_matrix[y][x] = sum(matrix1[y][i] * matrix2[i][x] for i in range(n)) % 1000
    return new_matrix

def matrix_pow(matrix, exp):
    n = len(matrix)
    # 단위 행렬로 시작
    result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

    while exp > 0:
        if exp % 2 == 1:
            result = multi_plex(result, matrix)
        matrix = multi_plex(matrix, matrix)
        exp //= 2
    
    return result

answer = matrix_pow(graph, B)

for row in answer:
    print(' '.join(map(str, row)))
