import sys
n,m = map(int,sys.stdin.readline().strip().split())
passwords = {}
for i in range(n):
    web, password = sys.stdin.readline().strip().split()
    passwords[web] = password
for i in range(m):
    web = sys.stdin.readline().strip()
    print(passwords[web])