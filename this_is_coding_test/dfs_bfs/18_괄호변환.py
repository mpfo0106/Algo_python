# 균형잡힌 괄호열 << 올바른 괄호 문자열

# 균형 괄호 -> 올바른 괄호
# 1. u,v 로 분리. u는 균형 x여야해
# 2. u가 균형이 맞으면, 다시 uv 분리 후 u에 붙여
# 3. u가 균형 x 면, 빈 문자열에 ( 붙여
# 3-1.

# 균형잡힌 문자열
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 문자열인가 확인
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면,
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

p = "()))((()"
print(solution(p))