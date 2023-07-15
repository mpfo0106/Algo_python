a,b = map(int,input().split())
if a <b: # 무조건 a가 더 크게
    tmp = b
    b =a
    a = tmp
cf =b
while True:
    if a%cf ==0 and b%cf ==0:
        break
    else:
        cf -=1
lcm = cf* (a//cf)*(b//cf)
print(cf)
print(lcm)

#TODO 유클리드 호제법
a,b = map(int,input().split())
def gcd(a,b):
    while b:
        a,b = b,a%b
        return a
c=gcd(a,b)
print(c)
print(a*b // c)