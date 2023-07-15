import sys
from itertools import combinations
n,m= map(int,sys.stdin.readline().split())
li = list(map(int,(sys.stdin.readline().split())))
tot =0
com = combinations(li,3)
for i in com:
    if tot < sum(i) <= m:
        tot = sum(i)
print(tot)

#TODO 조합으로 풀기! + 3중 for로도 풀 수 있다

'''
n, m = map(int, input().split())
l = sorted(map(int, input().split()), reverse=True)

s = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            t = l[i] + l[j] + l[k]
            if t <= m:
                s.add(t)
                break
print(max(s))
'''