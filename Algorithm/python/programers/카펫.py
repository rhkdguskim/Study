# yellow를 기준으로 가로로 배치되었을때, 세로로 배치되엇을때 둘다 따져본다.
    # ex) yellow가 3라면 1x3, 3x1
    # ex) yellow가 4라면 1x4, 2x2, 4x1
    # ex) yellow가 5라면 1x5, 5x1
    # ex) yellow가 6라면 1x6, 2x3, 3x2, 6x1
    # 즉 yellow가 n이라면 1~n까지 나누어 떨어지는 수를 구한다.
    # yellow들의 후보가 주어지만 이제 나머지 brown 개수를 구한다.
    # yellow가 1x6 일때, brown은 3x8 이다.
    # yellow가 n*m 일때, brown은 (n+2)*(m+2) 이다.
    # brown의 개수 (n+2)*(m+2) - (n*m) 이때 리턴하면 된다.

def solution(brown, yellow):
    return list(map(lambda x:(x[0]+2, x[1]+2),
                    filter(lambda x:x[0] >= x[1] and brown == (x[0]+2)*(x[1]+2) - yellow,
                           [(n, yellow // n) for n in range(1, yellow + 1) if yellow % n == 0])))[0]