# 개수가 한정적
# if target  arr1 arr2
#   target +=1
#
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
target = 1
for x in arr:
    if target < x:
        break
    target += x
print(x)