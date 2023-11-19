import heapq
n = int(input())
heap = []
ans = []
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            low =heapq.heappop(heap)
        else:
            low = 0
        ans.append(str(low))
    else:
        heapq.heappush(heap,x)

result = '\n'.join(ans)
print(result)