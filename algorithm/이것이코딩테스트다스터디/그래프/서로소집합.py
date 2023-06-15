# 특정 원소가 속하는 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else :
        return x

# 두원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent ,b)
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# parent 테이블에 값을 넣어준다.
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a , b)
    
# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, parent[i]))
    
    
# 경로 압축 기법을 사용한 find_parent 함수
def find_paraent(parent, x):
    if(parent[x] != x):
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]