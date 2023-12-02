# TODO // step 배열로 다시풀어보기

# 8x8 에서 나이트가 갈 수 있는 경우의 수
# 양 테투리라면 갈수 있는 경우가 2개뿐 + 2
# a1,8 면 2
# a2,7 면 3
# a3~6 면 4
# b,g열이면 최대6
# c~f 면 최대 8개
# str = input()
# cnt = 8
# col = str[0]
# row = int(str[1])
#
# if col == 'a' or col == 'h':
#     cnt -= 4
# elif col == 'b' or col == 'g':
#     cnt -= 3
# if row == 1 or row == 8:
#     cnt -= 2
# elif row == 2 or row == 7:
#     cnt -= 1
#
# print(cnt)

str = input()
col = int(ord(str[0]) - int(ord('a'))) + 1  # ord 는 아스키코드(유니코드)로
row = int(str[1])
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1
print(result)
