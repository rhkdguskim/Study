# 숫자 카드 게임은 여러개의 숫자 카드중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임이다.
# 먼저 뽑고자 하는 카드가 포함되어있는 행을 선택한다.
# 그다음 선택된 행에 포함된 카드들 중 가장 낮은 카드를 뽑아야한다.
# 따라서 처음에 카드를 골라낼 행을 선택할때, 
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략해야한다.

# 1) 행을 선택할때 최소값이 가장 큰 값을 갖는 행을 찾아야한다.

n , m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

maxvalue = 0
maxidx = 0
for i in range (len(arr)):
    if ( maxvalue < min(arr[i])):
        maxvalue = min(arr[i])
        maxidx = i

print(min(arr[maxidx]))