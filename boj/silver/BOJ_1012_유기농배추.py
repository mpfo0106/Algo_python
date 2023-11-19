# import sys
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# def dfs(x,y): #상하좌우 확인
#    stack = [(x,y)] # 방문할 노드를 추적
#    while stack: #스택이 비워질때까지
#        x,y = stack.pop()
#        if not visited[x][y]:
#           visited[x][y] = True
#        for i in range(4):
#            nx, ny = x+ dx[i], y+dy[i]
#            if nx<0 or nx >=m or ny<0 or ny >=n:
#                 continue #어차피 안쪽에 있는애가 건들여서 도는게 더 좋으니
#            if graph[nx][ny] and not visited[nx][ny]:
#                stack.append((nx,ny))# 방문안한애들 push
#
#
# t = int(sys.stdin.readline())
# for i in range(t):
#     m,n,k = map(int, sys.stdin.readline().split(" "))
#     visited = [[False]*n for _ in range(m)]
#     graph = [[0] * n for _ in range(m)]
#     cnt = 0
#     for i in range(k):
#         x,y = map(int,sys.stdin.readline().split(" "))
#         graph[x][y] = 1
#     cnt =0
#     for i in range(m):
#         for j in range(n):
#             if graph[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 cnt+=1
#     print(cnt)














import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny] and not visited[nx][ny]:
                stack.append((nx,ny))

t = int(sys.stdin.readline())
for i in range(t):
    m,n,k = map(int,sys.stdin.readline().split(" "))
    visited = [[False]*n for _ in range(m)]
    graph = [[0]*n for _ in range(m)]
    for j in range(k):
        x,y = map(int, sys.stdin.readline().split(" "))
        graph[x][y] = 1
        cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] and not visited[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt)





