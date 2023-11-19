import sys
import copy
from collections import deque
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
time = [0]* (N+1)
indegree = [0] *(N+1)
for i in range(1,N+1):
    lines = list(map(int,sys.stdin.readline().split()))
    time[i] = lines[0]
    for x in lines[1:-1]: #1~ 마지막 바로 전까지 선수 번호들
        indegree[i] +=1
        graph[x].append(i) #TODO 선수번호에 i 가 포함되어야함

def topology_sort():
    result = copy.deepcopy(time) # 리스트의 값을 복제
    q = deque()
    for i in range(1,N+1): #진입차수 0 인거부터 시작
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -=1
            if indegree[i] ==0:
                q.append(i)
    for i in range(1,N+1):
        print(result[i])



topology_sort()