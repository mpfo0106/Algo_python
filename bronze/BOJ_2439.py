import sys
nums = list(map(int,sys.stdin.readline().split()))
sum =0
for i in nums:
    sum += (lambda x:x**2)(i)
print(sum%10)
