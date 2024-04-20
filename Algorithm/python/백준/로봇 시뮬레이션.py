# https://www.acmicpc.net/problem/2174
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

robots = [(0, 0, 0)]
command = []

def L(direciton):
    if direciton == 'W':
        return 'S'
    
    if direciton == 'S':
        return 'E'

    if direciton == 'E':
        return 'N'
    
    if direciton == 'N':
        return 'W'
    
def R(direciton):
    if direciton == 'W':
        return 'N'
    
    if direciton == 'N':
        return 'E'

    if direciton == 'E':
        return 'S'
    
    if direciton == 'S':
        return 'W'
    
def F(y, x, direction):
    if direction == 'W':
        return y, x-1
    
    if direction == 'S':
        return y+1, x
    
    if direction == 'E':
        return y, x+1
    
    if direction == 'N':
        return y-1, x
    
def check_crash(robot, y, x):
    for i in range(1, len(robots)):
        if robots[i] != robot:
            r_y, r_x, _ = robots[i]
            if r_y == y and r_x == x:
                return i
    
    return 0
            
def is_range(y, x):
    return B > y >= 0 and A > x >=0

for _ in range(N):
    x, y, dir = map(str, input().split())
    robots.append((B-int(y), int(x)-1, dir))
    
for _ in range(M):
    robot, cmd, cnt = map(str, input().split())
    command.append((int(robot), cmd, int(cnt)))

is_crashed = False

for robot, cmd, cnt in command:
    y, x, dir = robots[robot]
    
    if cmd == 'L':
        cnt %= 4
        for _ in range(cnt):
            dir = L(dir)
            
    elif cmd == 'R':
        cnt %= 4
        for _ in range(cnt):
            dir = R(dir)
    elif cmd == 'F':
        for _ in range(cnt):
            if is_crashed:
                break
            
            y, x = F(y, x, dir)
            crash_robot = check_crash(robot, y, x)
            if crash_robot:
                is_crashed = True
                print("Robot %d crashes into robot %d" % (robot, crash_robot))
            
            if not is_range(y, x):
                is_crashed = True
                print("Robot %d crashes into the wall" % robot)
    
    robots[robot] = (y, x, dir)
    
if not is_crashed:
    print("OK")