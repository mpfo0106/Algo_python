# import sys
# n = sys.stdin.readline()
# nums =list(map(int,sys.stdin.readline().split()))
# big=small = nums[0]
# for i in nums:
#     if big < i:
#         big=i
#     if small > i :
#         small = i
# print(small , big)

#TODO max, min으로 걍 조짐
import sys
n = sys.stdin.readline()
nums =list(map(int,sys.stdin.readline().split()))
print(min(nums),max(nums))