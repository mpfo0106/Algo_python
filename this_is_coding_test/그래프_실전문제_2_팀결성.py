import sys
def union_parent(parent,a,b):
    a =find_parent(parent,a)
    b =find_parent(parent,b)
    if a<b:
        parent[b] =a
    else:
        parent[a] = b

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

n,m = map(int,sys.stdin.readline().split()) # n은 0~번호, m은 연산의 개수
parent = [0] *(n+1)

for i in range(n+1): #자기 자신 초기화
    parent[i] = i

for _ in range(m):
    isFind, a,b = map(int,sys.stdin.readline().split())
    if isFind == 0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")