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
    
    
def soulution(i, rgb):
    if i > N:
        return 0
    
    if i==N-1:
        return color[rgb][i]
    result=0
    for char in RGB:
        if rgb not in char:
            sol = soulution(i+1, char)
            cost = sol + color[rgb][i]
            print("sol", sol, 'color',color[rgb][i], rgb)
            if cost > result:
                result = cost

    return result

for char in RGB:
    print(char)
    print(soulution(0,char))