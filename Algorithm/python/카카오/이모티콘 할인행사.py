# https://school.programmers.co.kr/learn/courses/30/lessons/150368


# 이모티콘은 각각 10%, 20%, 30%, 40% 할인한다. ( 경우의수 4^7 )
# 유저는 유저가 선택한 할인율보다 이모티콘 할인율이 높은경우 이모티콘을 산다. ( 유저는 최대 100 명)
# 유저는 이모티콘을 다 샀다면, 유저가 선택한 금액보다 높을경우 이모티콘 서비스에 가입한다. 그렇지 않을경우 그냥 이모티콘을 산다.

# 유저수 * 이모디콘수 * (할인의 경우의수 4^7 = 16,384) = 100 * 7 * 16384


# 1. 유저를 순회하면서 유저가 이모티콘을 샀을때의 가격을 책정한다. ( 할인율의 계산으로 )
# 2. 만약 금액보다 높다면 서비스에 가입, 그렇지 않을경우 가격 책정
# 3. 모든유저를 순회한뒤 서비스에 가입한사람과, 가격을 temp 배열에 넣는다.
# 4. temp 배열을 서비스에 가입한사람의 내림차순, 가격 내림차순으로 정렬하여 첫번재 원소를 리턴한다.

# 이모티콘 할인율과 
discounts = [10, 20, 30 ,40]

def solution(users, emoticons):
    emotion_discont([], users, emoticons, [], [])
    new_arr = emotion_discont([], users, emoticons, [], [])
    new_arr.sort(key=lambda x:(-x[0], -x[1]))
    return [new_arr[0][0], new_arr[0][1]]

def emotion_discont(array, users, emoticons, new_emoicons, visited):
    
    if len(new_emoicons) == len(emoticons):
        # 여기서 유저 정보를 갱신한다.
        reg_cnt = 0 # 이모티콘 플러스에 가입한 회원수
        total_charge = 0 # 이모티콘을 구입한 가격
        for user in users:
            discount_rate = user[0]
            max_money = user[1]
            
            charge = 0
            for emo, discount in new_emoicons:
                if discount >= discount_rate: # 할인율이 더 높다면 이모티콘을 산다.
                    charge += int(emo * (100 - discount) / 100)

            if charge >= max_money: # 서비스 가입자
                reg_cnt += 1
            else:
                total_charge += charge
        
        array.append((reg_cnt, total_charge))
        return
    
    
    for emo in emoticons:
        for discount in discounts:
            if emo not in visited:
                new_emoicons.append((emo, discount))
                visited.append(emo)
                emotion_discont(array, users, emoticons, new_emoicons, visited)
                new_emoicons.pop()
                visited.pop()
    
    return array

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))