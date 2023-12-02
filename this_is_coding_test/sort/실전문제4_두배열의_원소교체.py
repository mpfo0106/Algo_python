# K번의 바꿔치기로 A합이 최대가 되게
import sys

n, k = map(int, sys.stdin.readline().split())
arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))
arr_A.sort()
arr_B.sort(reverse=True)
sum = 0
for i in range(k):
    if arr_A[i] <arr_B[i]:
        arr_A[i], arr_B[i] = arr_B[i], arr_A[i]
    else:
        break

print(sum(arr_A))
