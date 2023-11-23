# # s 초가 지난 후에 x,y 에 존재하는 바이러스의 종류
# # bfs 를 하는데 1초가 지나면 주변에 있는거 다 넣는거야.
# # 기존 흰 부분 =0 으로 두고 칠하기
#
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())  # k 는 바이러스 수
# arr = []
# virus = deque()
# for _ in range(n):
#     line = list(map(int, sys.stdin.readline().split()))
#     arr.append(line)
# s, a, b = map(int, sys.stdin.readline().split())
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# i = 1
# for x in range(len(arr)):
#     if i > k:
#         break
#     for y in range(len(arr[x])):
#         if arr[x][y] == i:
#             virus.append((x, y))
#             i += 1
#
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         a, b = queue.popleft()
#         type = arr[a][b]
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < n:  # 되는 경우
#                 if arr[nx][ny] == 0:
#                     arr[nx][ny] = type
#                     virus.append((nx, ny))
#
#
# for i in range(s):
#     for j in range(k):
#         virus_x, virus_y = virus.popleft()
#         bfs(virus_x, virus_y)
#
# print(arr[a - 1][b - 1])
#
# # bfs 에 넣는 바이러스가 갱신이 안되고있음. 바이러스 새로 갱신했으면 그걸 넣어줘야함.

#TODO 1.graph 그리면서 바이러스를 받아
# 2.bfs 진행하면서 타입,초,x,y 를 동시에 받아
# 3.

from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
virus = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))  # 바이러스 종류, 시간, 위치x,위치 y

# 낮은 번호 바이러스 우선임으로 정렬
virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:

    v_type, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동 가능할때
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            # 그 위치에 바이러스 넣기
            graph[nx][ny] = v_type
            q.append((v_type, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
