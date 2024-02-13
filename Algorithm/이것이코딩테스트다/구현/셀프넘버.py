def d(n):
    string = str(n)
    result = n
    for num in range(len(string)):
        result += int(string[num])
        
    return result

selfnumber = [1,3,5,7,9]
N = 10000
arr = [False] * N
for i in range(1, N):
    result = d(i)
    if result < N and arr[result] == False:
        arr[result] = True
    while result < N:
       result = d(result)
       if(result < N and arr[result] == False):
           arr[result] = True
       else : # 이미 찾은 데이터라면 중단.
           break

for i in range(1, len(arr)):
    if not arr[i]:
        print(i)