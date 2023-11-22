# #bfs
#
# # 안전 영역의 크기 최대를 구하기
# #벽은 3개 다 설치 0->1 로 변경
#
# #1. 2를 발견하면,
# # 2의 bfs 를 돌려야해.
#
# # 최대 배열은 8x8이며, 벽인 (1)을 세 번 모두 사용해야 합니다.
# # 따라서 (0,0)에서 시작하는 삼중 반복문을 통해 1을 배치하고 이때 최대 bfs 값인 0을 찾습니다.
#
# import sys
# from collections import deque
# n,m = map(int, sys.stdin.readline().split())
# graph = []
# for _ in range(n):
#     line = list(map(int,sys.stdin.readline().split()))
#     graph.append(line)
#
# def bfs(graph,start,visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# max_safe = 0
# empty_spaces = [(i,j) for i in range(n) for j in range(m) if graph[i][j] ==0]
# for i in range(len(empty_spaces)):
#     for j in range(i+1,len(empty_spaces)):
#         for k in range(j+1,len(empty_spaces)):
#             wall1 = empty_spaces[i]
#             wall2 = empty_spaces[j]
#             wall3 = empty_spaces[k]
#
#             graph[wall1[0]][wall1[1]] = 1
#             graph[wall2[0]][wall2[1]] = 1
#             graph[wall3[0]][wall3[1]] = 1
#
#             safe_area = bfs(graph)
#             max_safe = max(max_safe,safe_area)
#
#             graph[wall1[0]][wall1[1]] = 0
#             graph[wall2[0]][wall2[1]] = 0
#             graph[wall3[0]][wall3[1]] = 0

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 방향 에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# DFS 로 바이러스 퍼트리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상,하,좌,우 중 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:  # nx 는 행
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):  # temp 에 데이터 이전
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):  # 바이러스 만나면 퍼트려
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
