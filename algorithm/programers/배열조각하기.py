# 정수 배열 arr과 query가 주어집니다.
# query를 순회하면서 다음 작어블 반복합니다.

arr=[0,1,2,3,4,5]
query=[4,1,2]

def solution(arr, query):
    querylen = len(query)
    for i in range(querylen) :
        if i % 2 == 0 : # 짝수일때 뒤에걸 잘라야함
            if(query[i] != len(arr)) :
                arr = arr[0:query[i]+1]
        else : # 홀수일때 앞에걸 잘라야함
            if(query[i] == len(arr)) :
                arr = [arr[query[i]-1]]
            else :
                arr = arr[query[i]:len(arr)+1]
            
    return arr
            

solution(arr, query)