import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split(" "))
graph = [[0]*m for _ in range(n)]
# tomato= [] # 익은 토마토 좌표
visited = set()
queue = deque()
for i in range(n):
    line = list(map(int,sys.stdin.readline().strip().split(" ")))
    for j in range(m):
        graph[i][j] = line[j]
        if line[j]== 1:
            queue.append([i,j])
            # tomato.append([i,j])
            visited.add([i,j])

while queue:
    node = queue.popleft()
    # xy = tomato.pop()
    x,y = node[0],node[1]
    for neighbor in graph[x][y]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
