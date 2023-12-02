# 하나 잡으면 홀수로만 or 두개 건너띄기

n = int(input())
d = [0] * 1001
arr = list(map(int, input().split()))
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(3, n + 1):
    d[i] = max(d[i - 2] + arr[i], d[i - 1])  # 1을 선택하고 3을 선택 vs 2를 선택하고 3을 버릴때

print(d[n - 1])
