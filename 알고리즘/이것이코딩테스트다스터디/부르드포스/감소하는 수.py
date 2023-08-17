# https://www.acmicpc.net/problem/1038
# N번째 감소하는 수를 출력

N = int(input())

decrease_num = [[] for _ in range(10)]
for i in range(10):
    decrease_num[i].append(i)

for i in range(1,10):
    new_decrease_num = [[] for _ in range(10)]
    new_decrease_num[0].append(0)
    for j in range(10):
        for num in decrease_num[j]:
            print(num)
        if i > j:
            new_decrease_num[i].append(list(num for num in decrease_num[j]))
    
    print(new_decrease_num)
    decrease_num = new_decrease_num
        
        