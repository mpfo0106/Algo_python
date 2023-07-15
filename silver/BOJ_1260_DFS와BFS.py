import sys

n,m,v = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    temp_list = list(map(int,sys.stdin.readline().split()))
    graph[temp_list[0]].append(temp_list[1])
    graph[temp_list[1]].append(temp_list[0])

for i in range(n+1):
    graph[i].sort()

print(graph)
