import sys
N = int(sys.stdin.readline())
roads = list(map(int,sys.stdin.readline().split())) #도로의 길이
oils = list(map(int,sys.stdin.readline().split())) #기름값
result = oils[0]*roads[0]
min_oil_price = oils[0]
for i in range(1,N-1):
    min_oil_price = min(min_oil_price, oils[i]) #min 사용하지 말고 if price[i] <m 으로 하면 좀더 시간 이득이야
    result += roads[i]*min_oil_price
print(result)