import sys
n,m = map(int,sys.stdin.readline().split())
ans = [[0]*m for _ in range(n)]
array = []
x,y =0,0
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        array[i][j] = line[j]
        if line[j] ==2:
            x,y = i,j
