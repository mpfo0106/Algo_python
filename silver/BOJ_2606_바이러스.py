import sys
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

n = int(sys.stdin.readline()) # 노드의 개수
m = int(sys.stdin.readline()) # 간선의 개수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int,sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = set()

dfs(visited, graph, 1)
print(len(visited)-1)
