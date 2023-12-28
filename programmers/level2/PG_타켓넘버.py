# 숫자 2~20
# 1번이 음수일때 ,n 번이 음수일때...


# 배열의 모든 숫자를 더한 값이 타겟과 같으면 1, 아니면 0 리턴
# 재귀호출 두번해야함

numbers = [1, 1, 1, 1, 1]
target = 3

cnt = 0


def solution(numbers, target):
    cur_sum = 0
    idx = 0
    dfs(idx, cur_sum, numbers, target)
    return cnt


def dfs(idx, cur_sum, numbers, target):
    global cnt
    if idx == len(numbers):
        if cur_sum == target:
            cnt += 1
        return
    dfs(idx + 1, cur_sum + numbers[idx], numbers, target)
    dfs(idx + 1, cur_sum - numbers[idx], numbers, target)


print(solution(numbers, target))


# DP로
# 2차원 DP 테이블이 필요합니다.
# 첫 번째 차원은 '숫자' 배열의 각 인덱스를 나타내고,
# 두 번째 차원은 해당 인덱스에서 얻을 수 있는 가능한 합계를 나타냅니다.
# 두 번째 차원의 크기는 가능한 합계 범위(음수 합계에서 양수 합계까지)를 수용할 수 있을 만큼 커야 합니다.


# 합계가 음수일 수 있지만 배열 인덱스는 그럴 수 없으므로 합계가 항상 음수가 아닌지 확인하기 위해 합계를 상쇄해야 합니다.
# 이 오프셋은 'sum(numbers)'입니다.

def solution(numbers, target):
    total_sum = sum(numbers)
    offset = total_sum

    dp = [[0 for _ in range(2 * total_sum + 1)] for _ in range(len(numbers))]

    dp[0][numbers[0] + offset] = 1
    dp[0][-numbers[0] + offset] += 1 # 첫번째 숫자가 0인경우를 방지

    for i in range(1, len(numbers)):
        for j in range(2 * total_sum + 1):
            if dp[i - 1][j] != 0:
                dp[i][j + numbers[i]] += dp[i - 1][j]
                dp[i][j - numbers[i]] += dp[i - 1][j]

    return dp[len(numbers) - 1][target + offset]


print(solution(numbers, target))
