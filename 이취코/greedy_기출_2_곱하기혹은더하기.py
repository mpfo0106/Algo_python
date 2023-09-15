# 1 성공
nums = [int(char) for char in input()]
result = 1
for num in nums:
    if num >1:
        result *= int(num)
    else:
        result+=num

print(result)