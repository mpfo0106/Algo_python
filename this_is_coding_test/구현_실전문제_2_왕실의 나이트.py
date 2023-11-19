# status = list(input())
# cnt = 8
# if status[1] == '1' or status[1] == '8':
#     cnt -= 2
#     if status[0] == 'a' or status[0] == 'h':  # 가로 2칸 불가
#         cnt -= 4
#     elif status[0] == 'b' or status[0] == 'g':
#         cnt -= 2
# elif status[0] == 'a' or status[0] == 'h':
#     cnt -= 2
#     if status[1] == '1' or status[1] == '8':  # 가로 2칸 불가
#         cnt -= 4
#     elif status[1] == '2' or status[1] == '7':
#         cnt -= 2
#
# print(cnt)
input_data = input()
row = int(input_data[1])
column = int(input_data[0]) - int(ord('a'))+1
steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

cnt = 0
for step in steps:
    next_row = row +step[0]
    next_column = column + step[1]
    if next_row>=1 or next_row<=8 and next_column >=1 or next_column<=8: #영역을 안넘는 것들
        cnt+=1
print(cnt)
