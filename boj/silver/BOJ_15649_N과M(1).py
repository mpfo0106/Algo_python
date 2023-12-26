# 정리하면 배열의 길이가 3을 넘는지 확인하고,
# 넘는다면 출력 밑 return을 하고,
# 아니라면 배열을 순서대로 채우면 되는 것이다.

import sys

n, m = map(int, sys.stdin.readline().split())
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return ans
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()

back()
