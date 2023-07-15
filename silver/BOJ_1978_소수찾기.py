#TODO 소수인지 판별 할 자연수의 제곱근을 기준으로 그 숫자의 약수들의 곱셈은
# 대칭적으로 곱셈이 일어나게 됩니다.
# 따라서 소수인지 판별할때는 그 자연수의 제곱근 이하의 수까지만 검사를 하면 됩니다
n = int(input())
s = list(map(int,input().split()))
prime =set([])
for i in s: # 리스트를 돌리는게 더 낫다
    if s[i]==2: # if i<=1 로 1에대한 조건, 2 에 대한 스킵이 더 낫다
        prime.add(s[i])
        continue
    for j in range(2,s[i]):
        if s[i]% j == 0 :
            break
        if j == s[i]-1:
            prime.add(s[i])
print(len(prime))

'''
제곱근 이용 풀이, 함수만들고,  True False에 따라 cnt

import sys
import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
for j in l:
    if is_prime(j):
        cnt += 1
print(cnt)
'''