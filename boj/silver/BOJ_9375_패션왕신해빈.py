import sys

t = int(sys.stdin.readline())
ans=[]
for _ in range(t):
    clothes = {}
    total = 1
    n = int(sys.stdin.readline())
    if n ==0:
        cnt =0
    for _ in range(n):
        li = sys.stdin.readline().split()
        category = li[1]
        count = clothes.get(category,0) #키가 없으면 0
        clothes[category] = count+1

    for item in clothes.values():
        total *= (item+1)
    ans.append(total-1)
for i in ans:
    print(i)

