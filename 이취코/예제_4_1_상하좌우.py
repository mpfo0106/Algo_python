# import sys
# n = int(sys.stdin.readline())
# steps = list(sys.stdin.readline().split())
# x,y = 1, 1
# while steps:
#     step = steps.pop(0)
#     if step == "L":
#         if x ==1 :
#             continue
#         else:
#             x -=1
#     elif step == "R":
#         if x ==n:
#             continue
#         else:
#             x +=1
#     elif step == "U":
#         if y ==1:
#             continue
#         else:
#             y-=1
#     elif step == "D":
#         if y ==n:
#             continue
#         else:
#             y+=1
# print(str(y)+ " "+ str(x))
n = input()
x,y =1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x +dx[i]
            ny = y + dy[i]
        if nx <1 or ny <1 or nx>n or ny>n:
            continue
        x,y = nx,ny
print(x,y)