# https://www.acmicpc.net/problem/1036
# 문자의 가중치를 계산한다.
# 가중치의값이 가장높은순으로 K개의 알파벳을 뽑는다.
# 이제 바꾼 문자를 계산한다.

import sys
from collections import defaultdict

VALUE_36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input = sys.stdin.readline
    
def to_36(number):
    d = list(VALUE_36)
    a, b = number // 36, number % 36
    w = d[b]
    return to_36(a) + w if a != 0 else w

value = defaultdict(int)

N = int(input())
char_list = []
for _ in range(N):
    char = str(input().strip())
    char_list.append(char)
    
K = int(input())
    
for c in char_list:
    for j in range(len(c)):
        # 자리에따른 가중치를 계산한다. (문자열을 뒤집은 다음 가중치를 더한다. j는 0부터 시작하기때문)
        value[c[::-1][j]] += 36 ** j

for key in value.keys():
    # 알파벳 가중치를 계산해준다.
    value[key] = value[key] * (35 - int(key, 36))

value = sorted(value.items())
# 가중치를 내림차순으로 정렬 한다. ( Z로 바꾸면 항상 값이 커지기때문에 가장 큰값을 바꿔야 합이 커진다. )
value.sort(key= lambda x:-x[1])

for i in value[:K]:
    for j in range(len(char_list)):
        # 해당 알파벳을 Z로 replace해준다.
        char_list[j] = char_list[j].replace(i[0], "Z")

sum_number = 0
# 모든 값을 더해준다.
for char in char_list:
    sum_number += int(char, 36)

# 더한값을 알파벳으로 변환해준다.
print(to_36(sum_number))