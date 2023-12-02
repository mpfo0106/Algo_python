# TODO X

# 왼쪽부터 갈곳을 정함
# 1. if 왼쪽에 안가본곳 있다면, 왼쪽으로 회전. 2. 한칸전진
# 2. if 왼쪽 다가봄 , 왼쪽으로 회전
# 3. if 다 가보거나, 바다 , 바라보는 방향 유지 후 뒤로
# 3-1 if 뒤가 바다면 종료
# 0 북 1 동 2남 3 서
# 0 육지, 1 바다
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# a, b, my_d = map(int, sys.stdin.readline().split())
# direct = [0, 1, 2, 3]
# arr = []
# for _ in range(a):
#     arr.append(list(map(int, sys.stdin.readline().split())))
# while True:
#     if my_d == 0:  # 북쪽
#         if arr[a][b - 1] == 0:  # 육지라면
#             my_d -= 1
#             b = b - 1
#             arr[a][b] = 1
#         else:
#             my_d -= 1
n, m = map(int, input().split())
# 방문한 위치를 저장하기위한 맵을 생성해 0으로 초기화
d = [[0] for _ in range(n)]
# 현재 캐릭터의 x,y 좌표
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
