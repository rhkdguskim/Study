# https://www.acmicpc.net/problem/7568
N = int(input())
people = []
for _ in range(N):
    x ,y = map(int, input().split())
    people.append((x,y))
    
score = [1 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                score[i] += 1
                
print(*score)