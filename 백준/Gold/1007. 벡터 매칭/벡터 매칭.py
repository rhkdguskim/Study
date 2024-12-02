import math
from itertools import combinations

def calculate_min_vector_sum(points):
    n = len(points)
    total_x = sum(x for x, y in points)
    total_y = sum(y for x, y in points)
    min_length = float('inf')

    for comb in combinations(points, n // 2):
        sum_x = sum(x for x, y in comb)
        sum_y = sum(y for x, y in comb)

        diff_x = total_x - 2 * sum_x
        diff_y = total_y - 2 * sum_y

        length = math.sqrt(diff_x**2 + diff_y**2)
        min_length = min(min_length, length)

    return min_length


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        points = [tuple(map(int, input().split())) for _ in range(n)]
        results.append(calculate_min_vector_sum(points))

    for res in results:
        print(f"{res:.12f}")