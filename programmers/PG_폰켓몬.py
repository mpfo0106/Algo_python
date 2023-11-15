# def solution(nums):
#     max_num = len(nums)/2
#     if len(set(nums)) >= max_num:
#         answer = max_num
#     else:
#         answer = len(set(nums))
#     return answer

def solution(ls):
    return min(len(ls)/2, len(set(ls)))