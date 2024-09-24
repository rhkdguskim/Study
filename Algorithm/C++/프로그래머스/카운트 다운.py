import bisect

def solution(target):
    scores = [i for i in range(1, 21)]
    bull = 50
    # cnt값이 더작고, 싱글 또는 불을 더 많이 던진 선수가 승리
    def comp(v, r):
        if v[0] >= r[0]:
            if v[0] == r[0]:
                if r[1] > v[1] | r[2] > v[2]:
                    v = r
            else:
                v = r
                
        return v
    
    def dfs(target, cnt, single, double):
        if target == 0:
            return [cnt, single, double]
        
        
        v = [int(1e9), 0, 0]
        # 불보다 다음타겟이 큰경우
        # 불을던지던가 트리플 20 19, 18, 17 을 치던가.
        if target >= bull:
            return dfs(target - bull, cnt + 1, single, double)
        # 볼보다 작은경우는 
        else:
            # 1 ~ 49 이니까
            # 49 => 16 * 3 - 1 * 1
            # 48 => 16 * 3
            # 
            div = target % 3
            if div == 0:
                return [cnt + 1, single, double]
            
            div = target % 2
            if div == 0:
                return dfs(target)

            return [cnt + 1, single + 1, double]
        
    cnt, s, d = dfs(target, 0, 0, 0)
        
    answer = [cnt, s+d]
    return answer

print(solution(21))