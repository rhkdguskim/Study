# https://www.acmicpc.net/problem/1149
RGB = ['R', 'G', 'B']
color = dict()
color['R'] = list()
color['G'] = list()
color['B'] = list()

N = int(input())
for i in range(N):
    i, j, k = map(int, input().split())
    color['R'].append(i)
    color['G'].append(j)
    color['B'].append(k)
    
dp = []
def soulution(i, rgb):
    if i > N:
        return 0
    
    if i==N-1:
        return color[rgb][i]
    
    result = int(10e9)
    housepaint = color[rgb][i]
    for char in RGB:
        if rgb not in char:
            cost = soulution(i+1, char) + housepaint
            if result > cost:
                result = cost

    return result

for char in RGB:
    dp.append(soulution(0,char))