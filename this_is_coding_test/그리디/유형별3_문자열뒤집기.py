# 연속된 하나 이상의 숫자를 모두 뒤집기

# 다 0 다 1. 두번 나눠서
# 연속한 숫자면 cnt 안하고


# 0이면 다 거르고 1만 개수 세기

import sys

nums = list(sys.stdin.readline().strip())


def isStatus(statusNum):
    cnt = 0
    status = statusNum
    for num in nums:
        num = int(num)
        if num == statusNum:
            status = num
            continue
        else:
            if status == num:
                continue
            else:
                status = num
                cnt += 1
    return cnt


#### 답안 풀이
# print(min(isStatus(0), isStatus(1)))
#
# data = input()
# count0 = 0
# count1 = 0
#
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(data) - 1):
#     if data[i] != data[i + 1]:
#         if data[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0, count1))
