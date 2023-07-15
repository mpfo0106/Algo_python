t = int(input())
apt = [[0 for col in range(15)] for row in range(15)] #k행 n열 #
for i in range(15):
    apt[0][i] = i + 1
    apt[i][0] = 1
for i in range(14):
    for j in range(14):
        apt[i+1][j+1] = apt[i][j+1] + apt[i+1][j]
for i in range(t):
    k = int(input())
    n = int(input()) -1 # 1호부터 시작해서
    print(apt[k][n])