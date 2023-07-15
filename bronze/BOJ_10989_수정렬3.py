# import sys
# n = int(sys.stdin.readline().strip())
# li = []
# for i in range(n):
#     li.append(sys.stdin.readline().strip())
# li.sort() #TODO sort쓰면 메모리 부족 뜬다
# for j in li:
#     print(j)

#TODO 카운팅 정렬 해야해
import sys
n = int(sys.stdin.readline().rstrip())
cnt =[0]*10001

for i in range(n):
    cnt[int(sys.stdin.readline())] +=1

for i in range(10001):
    if cnt[i] != 0 :
        for _ in range(cnt[i]):
            sys.stdout.write(f"{i}\n")
