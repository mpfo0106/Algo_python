# X 부터 출발한 도시 중, 최단거리가 정확히 K인 모든 도시들의 번호를 출력
# 여러 상태를 봐야함으로 bfs 다.

# x 에서 출발해 거리가 k 가 되는걸 찾아야해
# queue 에 넣을때
import sys
from collections import deque


def bfs(graph, start, k, visited):
    queue = deque([start])
    visited[start] = True
    cnt =0
    while queue and k>cnt:
        if k ==1:
            return 
        v = queue.popleft()
        cnt+=1
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                cnt+=1
                visited[i] = True


# 도시 n , 도로 m , 거리 k, 출발 x
n, m, k, x = map(int, sys.stdin.readline().split(" "))
graph = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    visited = []
    bfs(graph, x, k, visited)
