# https://www.acmicpc.net/problem/5052
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {} # Dictionary 자료구조
        
class Trie:
    # 초기화 해드를 빈 노드로 설정
    def __init__(self):
        self.head = Node(None)

    # insert함수 - 트리를 생성하기 위한 함수
    def insert(self, string):
        # head노드부터 시작
        current_node = self.head
        
        # 문자열의 문자를 하나씩 확인
        for char in string:
            # 현재 노드의 자식중에 문자가 없다면
            if char not in current_node.children:
                # 자식 노드 추가
                current_node.children[char] = Node(char)
            # 자식 중에 문자가 있다면 current_node를 자식 노드로 변경
            current_node = current_node.children[char]
        
        # 문자열을 끝까지 탐색했다면 마지막 노드에 data추가
        current_node.data = string
        
    
    # Trie에서 접두사가있는지 찾는 함수
    def search_prefix(self, string):
        # head노드부터 시작
        current_node = self.head
        
        #문자열의 문자를 하나씩 확인
        for char in string:
            current_node = current_node.children[char]
        
        # 문자열이 탐색이 끝나면 children이 있는지 확인
        if current_node.children:
            return False
        else:
            return True

T = int(input())
for test_case in range(T):
    n = int(input())
    trie = Trie()
    arr = []
    for _ in range(n):
        char = input()
        arr.append(char)
        trie.insert(char)
    
    flag = True
    for chars in arr:
        if not trie.search_prefix(chars):
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')

