# 흰색 1 만 밟아.
# 최단경로, 가중치 없음 => bfs
#
from collections import deque

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[n-1][m-1]

print(solution(maps))
