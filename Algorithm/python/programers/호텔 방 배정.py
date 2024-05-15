# https://school.programmers.co.kr/learn/courses/30/lessons/64063
# 한번에 한명씩 순서대로 배정
# 고객은 투숙하기 원하는 방 번호를 제출
# 고객이 원하는 방이 비어있다면 즉시 배정
# 고객이 원하는 방이 이미 배정되어있다면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은방을 배정
import sys
sys.setrecursionlimit(int(1e9))

def solution(k, room_number):
    n = len(room_number)
    answer = []
    parent = {}
    
    def find(v):
        if v not in parent:
            parent[v] = v + 1
            return v
        parent[v] = find(parent[v])
        return parent[v]

    for number in room_number:
        available_room = find(number)
        answer.append(available_room)

    return answer
