INF = int(1e9)
n = int(input())
m = int(input()) #간선 개수
# 2차원 리스트만들고 초기화
graph = [[INF]* (n+1) for _ in range(n+1)]
# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
# 간선 정보 받기
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int,input().split())
    graph[a][b] =c

# 점화식에 따라 플로이드워샬
for k in range(1,n+1): # k 거쳐서
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] != INF:
            print(graph[a][b], end=" ")
