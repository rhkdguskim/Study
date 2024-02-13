# 부르트포스 문제로 모든 경우의수를 탐색해본다.
# 더하기를 한경우 빼기를 한경우 depth에따라서 숫자를 넣는다.
# depth가 7이되는경우는 종료한다. 중간중간 계산한값과, 현재 계속과정을 파라미터로 넘긴다.
# depth, sequence, sum
oper = ['+', '-', ' ']
def dfs(depth, sequence):
    if depth == N:
        newsequence = sequence.replace(' ', '')
        total = eval(newsequence)
        if 0 == total:
            ans.append(sequence)
            return
        else:
            return

    for op in oper:
        newsequence = sequence + op + str(depth+1)
        dfs(depth+1,newsequence)

T = int(input())

for i in range(T):
    N = int(input())
    ans = []
    dfs(1, '1')
    ans.sort()
    for temp in ans:
        print(temp)
    if T-1 > i:
        print()


