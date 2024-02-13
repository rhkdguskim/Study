def is_possible_channel(channel):
    if channel == 0:
        return 0 not in brokennumber

    while channel > 0:
        digit = channel % 10
        if digit in brokennumber:
            return False
        channel //= 10

    return True

def find_nearest_channel(target):
    min_push = abs(target - 100)  # 100에서 +, - 버튼으로만 이동하는 경우의 횟수

    for channel in range(1000001):
        if is_possible_channel(channel):
            press_count = abs(target - channel) + len(str(channel))
            min_push = min(min_push, press_count)

    return min_push

N = int(input())  # 목표 채널
M = int(input())  # 고장난 버튼 개수
brokennumber = []
if M > 0:
    brokennumber = list(map(int, input().split()))  # 고장난 버튼 리스트

print(find_nearest_channel(N))