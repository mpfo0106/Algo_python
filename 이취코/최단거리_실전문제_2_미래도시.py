import sys
INF = int(1e9)
# k -> x
n,m = map(int,sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
x,k = map(int,sys.stdin.readline().split())

for l in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][l]+ graph[l][b])
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)