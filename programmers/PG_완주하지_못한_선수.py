def solution(participant, completion):
    answer = ''
    li = {}
    for person in participant:
        if person in li:
            li[person] += 1
        else:
            li[person] = 1
    for person in completion:
        li[person] -= 1

    for person in li:
        if li[person] != 0:
            answer = person

    return answer


def __main__():
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    print(solution(participant, completion))


__main__()

# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
