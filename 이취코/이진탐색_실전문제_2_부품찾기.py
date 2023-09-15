# import sys
# def binary_search(array,start,end,target):
#     while start<=end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] >target:
#             end = mid-1
#         else:
#             start = mid+1
#         return None
#
# n = int(sys.stdin.readline())
# store = list(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# customer = list(map(int,sys.stdin.readline().split()))
# store.sort()
# for item in customer:
#     start = 0
#     end = len(store) - 1
#     isOk =binary_search(store,start,end, item)
#     if isOk:
#         print("yes")
#     else:
#         print("no")
###### 2번
# import sys
# n = int(sys.stdin.readline())
# store = list(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# customer = list(map(int,sys.stdin.readline().split()))
# li = [0]*1000001
# for i in store:
#     li[i] +=1
# for i in customer:
#     if li[i] ==1:
#         print("yes")
#     else:
#         print("no")
###### 3번 집합
import sys
n = int(sys.stdin.readline())
store = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
customer = list(map(int,sys.stdin.readline().split()))

for i in customer:
    if i in store:
        print()