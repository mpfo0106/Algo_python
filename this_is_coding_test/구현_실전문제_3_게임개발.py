import sys

n,m = map(int,input().split())
x,y,d = map(int,input().split())
visited = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
land = []
for _ in range(n):
    land.append(list(map(int,sys.stdin.readline().split())))
def turn_left():
    global d
    d -=1
    if d ==-1:
        d = 3
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and land[nx][ny] ==0: #안가봤을때 이동
        visited[nx][ny] = 1
        x = nx
        y = ny
        turn_time= 0
        cnt +=1
    else:
        turn_time +=1
        if turn_time ==4:
            nx = x-dx[d]
            ny = y-dy[d]
            if land[nx][ny] ==1:
                break
            else:
                x = nx
                y = ny
                turn_time =0
print(cnt)


