# x,+ 연산자를 넣어 만들 수 있는 가장 큰 수
# 모든 연산은 왼쪽에서부터

# 0만 피하고 다 곱하면 이득

nums = list(input())
sum = 0
for num in nums:
    num = int(num)
    if num == 0 or sum == 0:
        sum += int(num)
    else:
        sum *= int(num)

print(sum)

