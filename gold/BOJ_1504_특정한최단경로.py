import sys
import heapq
INF = int(1e9)
start = 1
N,E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,sys.stdin.readline().split())

def djikstra(start,graph,N):
    distance = [INF] * (N + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now =heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+ i[1]
            if cost < distance[i[0]]: # 다른노드로의 이동이 더 짧을 경우
                distance[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))
    return distance

distance_1 = djikstra(1,graph,N) # 1에서 시작해 N 까지 최단경로
distance_v1 = djikstra(v1,graph,N) # v1에서 시작해 N 까지 최단경로
distance_v2 = djikstra(v2,graph,N) # v2에서 시작해 N 까지 최단경로

route1 = distance_1[v1] + distance_v1[v2] + distance_v2[N] # v1 거쳤다가 v2 후 N
route2 = distance_1[v2] + distance_v2[v1] + distance_v1[N]  # v2 거쳤다가 v1 후 N

if route1 >=INF and route2 >=INF:
    print(-1)
else:
    print(min(route1,route2))

