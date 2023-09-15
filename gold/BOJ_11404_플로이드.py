import sys
INF = int(1e9)
n = int(sys.stdin.readline()) # n 은 도시개수 , m은 버스 개수
m = int(sys.stdin.readline())
graph = [[INF]* (n+1) for _ in range(n+1)]
for i in range(1,n+1): # 자기자신으로 가는건 0으로 초기화
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for _ in range(m):
    start,end,c = map(int,sys.stdin.readline().split()) #시작도시, 도착도시, 비용
    if graph[start][end] == INF:
        graph[start][end] = c
    else: #같은 노선이 두개 이상 들어올때 제일 작은 노선만 받기
        graph[start][end] = min(graph[start][end],c)

for k in range(1,n+1): #플루이드 워샬
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])
for i in range(1,n+1): # 출력
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j],end=" ")
    print()


#TODO 초기화
# for i in range(1, N + 1):
# dist[i][i] = 0

#TODO 값받기
# if c < dist[a][b]:
# dist[a][b] = c

#TODO 출력
# for row in dist[1:]:
# print(' '.join([str(el) if el != INF else '0' for el in row[1:]]))
