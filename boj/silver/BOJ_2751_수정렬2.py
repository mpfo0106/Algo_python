# import sys
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# arr.정렬()
# for j in arr:
#
#     #print(j)
import sys
input()
arr = sorted(list(map(int,sys.stdin.read().split())))
sys.stdout.write('\n'.join(map(str,arr)))