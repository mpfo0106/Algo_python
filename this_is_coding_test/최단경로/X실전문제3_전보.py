# 일방향성
# c에서 메세지 받는 도시의 개수,모두 받는데 걸리는 시간
# 플루이드 워샬
# TODO N,M 의 크기가 크기 때문에 다익스트라로 풀어야해.
import sys
import heapq

INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
cnt = 0
time = 0
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((z, y))


def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for z, y in graph[now]:
            cost = dist + z
            if cost < distance[y]:
                distance[y] = cost
                heapq.heappush(q, (cost, y))


djikstra(c)
for d in distance:
    if d != INF:
        cnt += 1
        time = max(time, d)

print(cnt - 1)
print(time)

# import sys
#
# INF = int(1e9)
# n, m, c = map(int, sys.stdin.readline().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# cnt = 0
# time = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             graph[i][j] = 0
#
# for _ in range(m):
#     x, y, z = map(int, sys.stdin.readline().split())
#     graph[x][y] = z
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for i in range(n):
#     if graph[c][i] < INF:
#         cnt += 1
#         time += graph[c][i]
#
# print(cnt, end=" ")
# print(time)
