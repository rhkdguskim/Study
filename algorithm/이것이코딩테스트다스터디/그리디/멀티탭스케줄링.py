# https://www.acmicpc.net/problem/1700

# 1) 현재 뽑으려는 큐안에 콘센트 안에 아이템이 없는경우 콘센트에서 뺀다.
# 2) 현재 뽑으려는 큐안에 다 있는경우 콘센트로 넣는 우선순위가 가장 낮은애의 자리를 뺀다.

N, K = map(int, input().split())
useorder = list(map(int, input().split())) # 콘센트에 꽂아야 하는 아이템 리스트들

multitap = [] # 멀티탭
plugoff = 0
for _ in range(len(useorder)):
    item = useorder.pop(0)
    mincount = int(10e9)
    idx = 0
    
    if item in multitap: # 이미 콘센트에 꽂혀있는경우
        continue
    
    if len(multitap) == N: # 멀티텝이 꽉찬경우 콘센트에있는 하나의 아이템을 뽑아야한다.
        # 콘센트에 꽂혀있는 아이템중에 꽂을 리스트에 없는 아이템을 찾는다.
        concentidx = 0
        maxindex = 0
        for i in range(len(multitap)):
            
            if not multitap[i] in useorder:
                multitap.pop(i) # 리스트에 없는경우 아이템을 pop하고 break 한다.
                plugoff += 1
                break
            else :
                cost = useorder.index(multitap[i])
                if cost > maxindex: # 제일 멀리있는 아이템 index를 구한다.
                    maxindex = cost
                    concentidx = i
            
    
    if len(multitap) == N: # 리스트에 콘센트들이 다 있다면.
        multitap.pop(concentidx)
        plugoff += 1

    multitap.append(item)
        
print(plugoff)