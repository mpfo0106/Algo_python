# 주어진 횟수만큼 선택정렬
# 예외는 횟수가 남았을때.
# 횟수가 남는다면 맨 마지막 두개를 와리가리


#### 일단 보류한다...
t = int(input())
for _ in range(t):
    nums, c = input().split()
    c = int(c)
    li = list(map(int, nums))

    for i in range(len(li)):
        if c<=0:
            break
        maxi = i

        for j in range(i + 1, len(li)):
            if li[maxi] <= li[j] and j-i <=c:   # j-i <= c 로 조건하나 더 추가
                maxi = j

        if maxi != i:
            for k in range(maxi, i, -1): #for 문에 -1씩 내려오면서 해결
                li[k], li[k-1] = li[k-1], li[k]
                c -= (maxi -i)
    result = ''.join(map(str,li))
    print(result)

