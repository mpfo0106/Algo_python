import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split()) #N이 K를 찾으러감

def bfs(start, visited,time):
    queue = deque([start])
    time[start] = 0
    visited[start] =True
    while queue:
        v = queue.popleft()
        next_v = v * 2  # 순간이동 할 때
        if 0 <= next_v <= 100000 and not visited[next_v]:
            queue.append(next_v)
            visited[next_v] = True
            time[next_v] = time[v]
        for next_v in [v-1,v+1]: # v-1, v+1 이면 1초
            if 0<= next_v <=100000 and not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True
                time[next_v] = time[v] +1
        if visited[K]:
            return time[K]

visited = [False] * 100001
time = [-1] * 100001 #위치별 시간
print(bfs(N,visited,time))

#### TODO 이런 스킬도
# 1. dx = [-1,1]
# for i in range(2):
#             nx = x + dx[i]

# 2. visited = [-1]*100001 로 두고 타임과 visited 를 한꺼번에 관리