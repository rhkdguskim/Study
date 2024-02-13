N , M = map(int, input().split())
ricecake = list(map(int, input().split()))

data = 0
def binary_search(target, start ,end):
    global data
    mid = (start+end)//2
    
    if(start > end):
        return
    
    result = 0
    for cake in ricecake:
        if(cake > mid):
            result += cake - mid
            
    if(result < M): # 왼쪽 부분 탐색
        binary_search(target, start, mid - 1)
    else : # 오른쪽 부분 탐색
        data = mid
        binary_search(target, mid + 1, end)
        

binary_search(M, 0, max(ricecake))
print(data)