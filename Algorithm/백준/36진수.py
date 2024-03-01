# https://www.acmicpc.net/problem/1036
# 문자의 가중치를 계산한다.
# 가중치의값이 가장높은순으로 K개의 알파벳을 뽑는다.
# 이제 바꾼 문자를 계산한다.
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
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
        value[c[::-1][j]] += 36 ** j

for key in value.keys():
    value[key] = value[key] * (35 - int(key, 36))

value = sorted(value.items())
value.sort(key= lambda x:-x[1])

for i in value[:K]:
    for j in range(len(char_list)):
        char_list[j] = char_list[j].replace(i[0], "Z")

sum_number = 0
for char in char_list:
    sum_number += int(char, 36)

print(to_36(sum_number))