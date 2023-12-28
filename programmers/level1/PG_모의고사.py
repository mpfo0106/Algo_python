# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,// 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,/// 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,/// 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


answers = []


def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    answer = []
    for i, ans in enumerate(answers):
        if ans == student1[i % 5]:
            score[0] += 1
        if ans == student2[i % 8]:
            score[1] += 1
        if ans == student3[i % 10]:
            score[2] += 1

    max_score = max(score)
    for i, item in enumerate(score):
        if max_score == item:
            answer.append(i + 1)
    return answer


solution(answers)
