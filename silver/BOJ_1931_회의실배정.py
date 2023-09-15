import sys
N = int(sys.stdin.readline())
time_table = [(0,0)] *(N)
result = 0
now_end = 0
for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    time_table[i] = (start,end)
time_table.sort(key= lambda x: (x[1], x[0])) # 끝나는 시간 우선 정렬, 동점자 있으면 빨리 시작하는 순서로
for time in time_table:
    start,end = time
    if now_end <=start:
        result+=1
        now_end = end

print(result)

#TODO 우선순위 큐로도 풀이 가능
# for _ in range(n) :
# start, end = map(int, input().split())
# heapq.heappush(m, (end, start))
