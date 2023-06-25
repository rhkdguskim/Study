# https://www.acmicpc.net/problem/1700
# 현재 꽂혀있는 아이템중 사용량이 제일 적을 것 같은 아이템을 뽑는다.

N, K = map(int, input().split())
useorder = list(map(int, input().split()))

multitap = []
plugoff = 0
for _ in range(len(useorder)):
    item = useorder.pop(0)
    mincount = int(10e9)
    idx = 0
    
    if item in multitap: # 이미 콘센트에 꽂혀있는경우
        continue
    
    if len(multitap) == N: # 멀티텝이 꽉찬경우 제일 적게 사용하게될 아이템을 뽑아야한다.
        for i in range(len(multitap)):
            numcount = useorder.count(multitap[i])
            if mincount > numcount:
                mincount = numcount
                idx = i
        
        multitap.pop(idx) # 가장 적게 사용하게될 아이템을 제거한다.
        plugoff += 1
        multitap.append(item) # 현재 아이템을 넣는다.
    else:
        multitap.append(item)
        
print(plugoff)