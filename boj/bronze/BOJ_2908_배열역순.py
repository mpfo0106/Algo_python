# import sys
# nums = list(sys.stdin.readline().strip().split())
# a = list(nums[0])
# b = list(nums[1])
# a.reverse()
# b.reverse()
# a= int(''.join(a))
# b= int(''.join(b))
# if a > b:
#     print(a)
# else:
#     print(b)

#TODO 배열 [::-1] 이용한 방법 + 문자열도 max가 되는구나
a,b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a,b))