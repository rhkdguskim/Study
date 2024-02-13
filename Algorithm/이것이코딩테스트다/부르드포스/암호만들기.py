# https://www.acmicpc.net/problem/1759
# 한개의 최소 한개 모음(a,e,i,o,u ), 최소 두개의 자음
# 모음이 없는경우는 패스
# 자음이 없거나 자음이 1개인경우 패스
import heapq

L, C = map(int, input().split()) # L : 알파벳 암호 개수 C: 사용문자 가지수
arr = input().replace(" ", "")
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u']

def isvowel(char): # 탐색개수를 줄여아한다.
    newchar = ''.join(char)
    vowelcounter = 0
    nvowelcounter = 0
    for chr in vowels:
        if chr in newchar:
            vowelcounter += 1 # 모음
        else :
            nvowelcounter += 1 # 자음
    if(vowelcounter >= 1 and nvowelcounter >= 2):
        return True
    else :
        return False
    
def alpavet(char) :
    newchar = ''.join(char)
    prev = newchar[0]
    for d in range(1, len(newchar)): #알파벳 순서가 맞지않으면 탐색을 종료한다.
        if(prev < newchar[d]):
            prev = newchar[d]
        else :
            return False
        
    return True

queue = []
def generate_n_dimensional_loop(dimensions, current_loop=[]):
    if len(current_loop) > 1 and not alpavet(current_loop) :
        return
    
    if len(current_loop) == len(dimensions):
        if isvowel(current_loop):
            heapq.heappush(queue, ''.join(current_loop))
        return

    for i in range(dimensions[len(current_loop)]):
        current_loop.append(arr[i])
        generate_n_dimensional_loop(dimensions, current_loop)
        current_loop.pop()

dimensions = [C] * L

generate_n_dimensional_loop(dimensions)

while queue:
    print(heapq.heappop(queue))