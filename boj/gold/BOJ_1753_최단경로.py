import sys
import heapq # 우선순위 큐
INF = int(1e9) #무한 정의
n, m = map(int,input().split()) #정점의 개수 v , 간선의 개수 e
k = int(input()) #시작 정점의 번호 K
graph = [[] for _ in range(n+1)] #인접리스트
distance = [INF for _ in range(n+1)] #최단거리 리스트

for i in range(n):
    u,v,w = map(int,input().split()) # u에서 v로 가는 가중치 w 간선
    graph[u].append((v,w))
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]: #현재 노드를 거쳐서 이동한 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)
for i in range(1,n+1):
    if distance[i]== INF:
        print("INF")
    else:
        print(distance[i])
