# https://www.acmicpc.net/problem/21608
import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
student_like = [set() for _ in range(N*N + 1)]
order_student = []

for _ in range(N*N):
    temp = list(map(int, input().split()))
    order_student.append(temp[0])
    for t in temp[1:]:
        student_like[temp[0]].add(t)
        
room = [[0 for _ in range(N)] for _ in range(N)]

def is_near_by(y1, x1, y2, x2):
    return 1 == (abs(y1-y2) + abs(x1-x2))

def get_bigest(near_dict):
    temp = []
    for key in near_dict:
        temp.append((near_dict[key], key[0], key[1]))
    
    temp.sort(reverse=True)
    
    result = []
    for t in temp:
        if temp[0][0] != t[0]:
            break
        
        if room[t[1]][t[2]] == 0:
            result.append((t[1], t[2]))

    return result

def first(likedstudent):
    queue = []
    near_dict = defaultdict(int)
    # 내가 좋아하는 학생찾기
    for i in range(N):
        for j in range(N):
            near_dict[(i, j)] = 0
            if room[i][j] in likedstudent:
                queue.append((i, j))

    # 가장 인접한 칸 찾기
    for i, j in queue:
        for i1 in range(N):
            for j1 in range(N):
                if is_near_by(i, j, i1, j1) and room[i1][j1] == 0:
                    near_dict[(i1, j1)] += 1
    
    return get_bigest(near_dict)

def second(queue):
    near_dict = defaultdict(int)
    
    for i, j in queue:
        near_dict[(i, j)] = 0
        for i1 in range(N):
            for j1 in range(N):
                if is_near_by(i, j, i1, j1) and room[i1][j1] == 0 and room[i][j] == 0:
                    near_dict[(i, j)] += 1
    
    return get_bigest(near_dict)
    
def third(queue : list):
    queue.sort(key=lambda x:(x[0], x[1]))
    return [queue[0]]
    

for student in order_student:
    queue = first(student_like[student])
    if len(queue) > 1:
        queue = second(queue)
        if len(queue) > 1:
            queue = third(queue)
            
    seat_pos = queue[0]
    room[seat_pos[0]][seat_pos[1]] = student
    
ans = 0

def get_score(like_cnt):
    if like_cnt == 0:
        return 0
    elif like_cnt == 1:
        return 1
    elif like_cnt == 2:
        return 10
    elif like_cnt == 3:
        return 100
    else:
        return 1000
    
for i in range(N):
    for j in range(N):
        student = room[i][j]
        like_cnt = 0
        for i1 in range(N):
            for j1 in range(N):
                if is_near_by(i, j, i1, j1) and room[i1][j1] in student_like[student]:
                    like_cnt += 1
    
        ans += get_score(like_cnt)
            
print(ans)