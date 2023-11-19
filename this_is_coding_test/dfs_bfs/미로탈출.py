# bfs. 1만 밟아서 탈출
N,M = map(int,input().split(" "))
graph = []
for i in range(N):
    line = list(map(int,input().split(" ")))
    for j in range(M):
        graph.append(line[j])