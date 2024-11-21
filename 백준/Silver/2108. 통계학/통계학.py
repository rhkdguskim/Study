import sys
from collections import defaultdict

input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]
nums.sort()

# 산술평균
avg = round(sum(nums) / len(nums))
print(avg)
# 중앙값
mid = nums[len(nums)//2]
print(mid)
# 최빈값
bcv = defaultdict(int)

for n in nums:
    bcv[n] += 1

tmp = [(bcv[key], key) for key in bcv.keys()]
tmp.sort(key=lambda x:(-x[0], x[1]))
if len(tmp) == 1:
    print(tmp[-1][1])
else:
    if tmp[0][0] == tmp[1][0]:
        print(tmp[1][1])
    else:
        print(tmp[0][1])

# 최대 - 최소
if len(nums) == 1:
    print(0)
else:
    print(nums[-1] - nums[0])