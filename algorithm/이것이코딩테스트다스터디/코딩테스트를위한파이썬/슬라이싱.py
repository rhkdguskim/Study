a = [1,2,3,4,5,6,7,8,9]

print(a[-1]) # 9를 출력
print(a[-3]) # 7을 출력
print(a[1:4]) # 1번 인덱스부터 3번인덱스까지 출력
print(a[1:]) # 1번 부터 마지막까지 출력
print(a[:1]) # 1번 부터 처음까지 출력

# 언더바 역할
# 반복을 수행하되 변수의 값을 무시하고자 할때 _ 를 사용한다.
for _ in range(5):
    print("Hello World!!")

array = [i for i in range(20) if i % 2 == 1] # 홀수만 출력합니다.
array2 = [0 for _ in range(20)]
array3 = [i*i for i in range(20)]
print(array)
print(array2)
print(array3)

a = [1,2,3,4,5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result)

# dict() 딕셔너리
# list() 배열
# set() 집합 (중복 불가능) -> add(), remove(), update()

print((lambda a, b : a+b)(3,7))

# itertools : 순열, 조합 라이브러리 제공
# heapq : 우선순위 큐
# bisect : 이진탐색 이용
# collection : deque, counter 등의 유용한 자료구조

from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2)) # 크기가 3인 모든 순열 구하기
print(result)

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
