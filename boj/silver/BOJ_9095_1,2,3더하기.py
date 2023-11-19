# import sys
# max = 10
# sum = [0] * (max+1)
# sum[0] = 0
# sum[1] = 1
# sum[2] = 2
# sum[3] = 4
# ans=[]
# for i in range(4,max+1):
#     sum[i] += sum[i-1] + sum[i-2] +sum[i-3]
#
# t = int(sys.stdin.readline().strip())
# for _ in range(t):
#     n = int(sys.stdin.readline().strip())
#     ans.append(sum[n])
# for i in ans:
#     print(i)
import sys

data = int(sys.stdin.readline())

for _ in range(data):
    num = []
    num.append(1)
    num.append(1)
    num.append(2)
    num.append(4)
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        num.append(num[i - 1] + num[i - 2] + num[i - 3])

    print(num[n])