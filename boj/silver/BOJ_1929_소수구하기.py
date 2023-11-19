#TODO 에라토스 체 이용
import sys
m, n = map(int,sys.stdin.readline().split())
li = [True]*(n+1)
li[0] =False
li[1] =False
for i in range(int(n**0.5)+1):
    if li[i]:
        for j in range(i*2,n+1,i):
            li[j] = False
for i in range(m,n+1):
    if li[i]:
        print(i)






'''prime=[True]*(n+1)
prime[0]=False
prime[1]=False
for a in range(len(prime)):
    if prime[a]:
        for b in range(a*2, n+1, a):
            prime[b]=False'''