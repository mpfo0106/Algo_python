## 1회

# 젤 큰놈부터 넣는거야. 근데 버려도돼.
import sys
from collections import deque
N = int(sys.stdin.readline())
fears = list(map(int,sys.stdin.readline().split()))
fears.sort()
result = 0
count = 0
for i in fears:
    count +=1
    if count>= i:
        result+=1
        count = 0
print(result)