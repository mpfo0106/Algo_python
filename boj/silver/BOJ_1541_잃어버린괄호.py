# nums = input().split("-")
# result = 0
# plus_num =nums[0].split("+")
# for i in plus_num:
#     result+=int(i)
# for num in nums[1:]:
#     real_num = num.split("+")
#     for i in real_num:
#         result -= int(i)
# print(result)

# TODO 효율적인 코드
nums = input().split("-")
result = sum(map(int,nums[0].split("+")))
for num in nums[1:]:
    result -= sum(map(int,num.split("+")))
print(result)