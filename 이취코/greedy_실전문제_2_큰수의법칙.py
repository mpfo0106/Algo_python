import sys
import time
start = time.time()
n,m,k = map(int,sys.stdin.readline().split(" ")) #배열크기 n , 숫자 더하는 횟수 m,최대 중복가능 k
line = list(map(int,sys.stdin.readline().split()))
line.sort(reverse=True)
tot =0

while True:
    for i in range(k):
        if m == 0:
            break
        tot += line[0]
        m-=1
    if m ==0:
        break
    tot += line[1]
    m-=1


#
# cnt = m//(k+1) # 횟수
# mod = m %(k+1)
# tot += cnt* (line[0] * k + line[1]) +mod * line[0]

print(tot)


end = time.time()
print(end-start)