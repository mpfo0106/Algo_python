# # X 부터 출발한 도시 중, 최단거리가 정확히 K인 모든 도시들의 번호를 출력
# # 최단경로 문제. 다익스트라 접근.
#
# import sys
# import heapq
#
# INF = int(1e9)
# # 도시 n , 도로 m , 거리 k, 출발 x
# n, m, k, x = map(int, sys.stdin.readline().split(" "))
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split(" "))
#     graph[a].append((1, b))  # 가중치 1
#
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:  # 이미 처리되었다면(거리가 짧아진거니)
#             continue
#         for i in graph[now]:
#             cost = dist + i[0]
#             if cost < distance[i[1]]:
#                 distance[i[1]] = cost
#                 heapq.heappush(q, (cost, i[1]))
#
#
# ans = []
# dijkstra(x)
# for i in range(1, n + 1):
#     if distance[i] == k:
#         ans.append(str(i))
#
# if not ans:
#     ans.append(str(-1))
#
# print("\n".join(ans))

# TODO BFS 로 푼것

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (n + 1)
distance[x] = 0


def bfs(start):
    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:  # 아직 방문 X 도시라면
                distance[next_node] = distance[now] + 1
                q.append(next_node)


bfs(x)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
