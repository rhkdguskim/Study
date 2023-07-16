# 다양한 수로 이루어진 배열이 있다. 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다.
# 특정한 인덱스 번호에 해당하는 수가 K번을 초과하여 더해질 수 있다

arr = [2,4,5,4,6]
m=8
k=3
result = 0
arr = sorted(arr, reverse=True)

counter = 0
kcounter = 0
arridx = 0
while(counter < m):
    if(arr.count(arr[arridx]) > 1): # count개수가 2개 이상이면 idx는 arridx는 여기서 멈춘다. 
        result += arr[arridx]
        counter += 1
    else : # count개수가 1개이면 idx는 k만큼 연산한뒤 하나 작은수를 더한뒤 다시 돌아온다.
        counter += 1
        kcounter += 1
        if(k > kcounter) :
            result += arr[arridx]
        else :
            result += arr[arridx + 1]
            kcounter = 0


# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰수
second = data[n-2] # 두 번째로 큰수

result = 0

while True:
    for i in range(k): # k번을 첫번째 큰수를 더하기
        if m == 0 :
            break
        result += first
        m -= 1
        if m == 0 : # 1번을 두번째 큰수를 더하기
            break
        result += second
        m -= 1