# https://www.acmicpc.net/problem/1700
import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
products = list(map(int, input().split()))

multi_tap = set()
ans = 0
for i in range(len(products)):
    if products[i] in multi_tap: # 이미 물품이 멀티탭에 있는경우
        continue
    
    if len(multi_tap) == N: # 멀티탭의 수가 꽉찬경우 (하나를빼서 현재 물품을 꽂아야한다.)
        max_idx = -1
        del_product = 101
        for p in multi_tap:
            try:
                idx = products[i:].index(p) # 현재위치로부터 가장 멀리있는 인덱스 찾기 ( 가장 나중에 장착될 전기용품 )
            except:
                # 제일 첫번째꺼가 골라짐.
                idx = K
            if max_idx < idx:
                del_product = p
                max_idx = idx

        ans += 1
        multi_tap.discard(del_product)

    multi_tap.add(products[i])

print(ans)
# 멀티탭 ( 멀티탭의 길이만큼만 확인해야한다, 아래의 예외사항을 생각해보자 )

# 1, 2, 3, 4, 5
# 6, 7, 8, 9, 10

# 2, 3, 5, 6
# 1, 3, 1, 2, 1, 1, 3, 2, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6

# 1,3,1,2 중에서 제일 카운팅이 작은 숫자를 고른다. (5, 6)
# 5를 빼보자 :3
# 1,2,3,5
# 6을 빼보자 :2
# 1,2,3,6


# 멀티탭 ( 멀티탭의 길이만큼만 확인해야한다, 아래의 예외사항을 생각해보자 )
# 멀티탭에서 해당 아이템을 뺐을때 추후에 나온다면 바꿔서 끼워야함으로, 가중치가 가장 낮은 애들 고른다.
# 1, 2, 3
# 6, 3, 1, 2, 1, 1, 3, 2, 5

# 가중치가 같다면 바뀌는 횟수도 같다.
# 2를 고를때
# 3번
# 3을 고를때
# 3번
