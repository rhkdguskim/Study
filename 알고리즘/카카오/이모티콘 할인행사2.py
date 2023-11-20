from itertools import product

discounts = [10, 20, 30, 40]

def solution(users, emoticons):
    best_combo = max(emotion_discount(users, emoticons), key=lambda x: (x[0], x[1]))
    return [best_combo[0], best_combo[1]]

def emotion_discount(users, emoticons):
    results = []
    for discount_combo in product(discounts, repeat=len(emoticons)):
        reg_cnt, total_charge = calculate_user_responses(users, emoticons, discount_combo)
        results.append((reg_cnt, total_charge))
    return results

def calculate_user_responses(users, emoticons, discount_combo):
    reg_cnt = 0
    total_charge = 0
    for user in users:
        discount_rate, max_money = user
        charge = sum(emo * (100 - discount) / 100 for emo, discount in zip(emoticons, discount_combo) if discount >= discount_rate)
        if charge >= max_money:
            reg_cnt += 1
        else:
            total_charge += charge
    return reg_cnt, total_charge

# 테스트
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))