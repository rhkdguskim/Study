# 버블정렬은 하나씩 비교해나가면서 가장 큰수를 오른쪽에 배치한다.
arr = {5,6,7,8,9,0,1,2,3,4}; # 배열 예제

def swap(a,b) :
    temp = a
    a = b
    b = temp
    return a,b

for a in arr:
    for b in arr-1:
        print(a,b)