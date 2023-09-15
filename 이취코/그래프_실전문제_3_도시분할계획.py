import sys
def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

N,M = map(int,sys.stdin.readline().split()) # N= 집의 개수, M= 길의 개수
#parent = [0]*(N+1)
edges = []
result = 0
# for i in range(1, N+1):
#     parent[i] = i
parent = [i for i in range(N+1)]
# for _ in range(M):
#     a,b,cost = map(int,sys.stdin.readline().split())
#     edges.append((cost,a,b))
lines = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
lines.sort(key=lambda x:x[2])
#edges.sort()
max_cost = 0
# for edge in edges:
#     cost,a,b = edge
#     if find_parent(parent,a) != find_parent(parent,b):
#         union_parent(parent,a,b)
#         result+= cost
#         max_cost = max(max_cost,cost) # 제일 코스트 큰 엣지를 뽑아서 빼
for line in lines:
    a,b,cost = line
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        max_cost = cost

print(result-max_cost)

#TODO 리스트 컴프리션을 잘 쓰자