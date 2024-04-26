def solution(N, number):
    if N == number:
        return 1

    num_set = [set() for _ in range(9)]
    num_set[1].add(N)

    for i in range(2, 9):
        for j in range(1, i):
            # 예를들어 4자리를 구한다면 (1, 3) (2, 2) (3, 1) 를 구하면 된다.
            for a in num_set[j]: # i가 4일때 1, 2 ,3
                for b in num_set[i - j]: # i가 4일때 3, 2, 1
                    num_set[i].update([a + b, a - b, b - a, a * b])
                    if b != 0:
                        num_set[i].add(a // b)
                    if a != 0:
                        num_set[i].add(b // a)
        num_set[i].add(int(str(N) * i))  # NN, NNN 등을 추가

        if number in num_set[i]:
            return i

    return -1
