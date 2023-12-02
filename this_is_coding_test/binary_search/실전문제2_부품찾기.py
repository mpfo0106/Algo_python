#
import sys

n = int(sys.stdin.readline())
store = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
customer = list(map(int, sys.stdin.readline().split()))
store.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return True
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        return False

ans = []
for item in customer:
    if binary_search(store, item, 0, len(store) - 1):
        ans.append("yes")
    else:
        ans.append("no")

print(" ".join(ans))