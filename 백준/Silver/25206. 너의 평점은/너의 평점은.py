import sys
input = sys.stdin.readline

score = {'A+' : 4.5, 'A0' : 4.0,
         'B+' : 3.5, 'B0' : 3.0, 
         'C+' : 2.5, 'C0' : 2.0,
         'D+' : 1.5, 'D0' : 1.0,
         'F' : 0.0 }

s_s = 0
s_v = 0
for _ in range(20):
    _, b, c = map(str, input().split())
    s = float(b)
    if c in score:
        s_s += s
        s_v += s*score[c]

print(round(s_v/s_s, 6))