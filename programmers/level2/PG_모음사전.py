# 길이 5이하 단어. 몇번째 단어인지 return

# 백트래킹으로 접근한다.
# 공백은 0으로 치환하고, 맨 처음부터 백트래킹으로 일일히 확인한다.
# words 와 같은 것을 확인했을때 cnt 를 출력한다.


# ans = []
# cnt = 0
# words = "AAAE"
# vowel_to_number = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
#
# word = [str(vowel_to_number[char]) for char in words]
# if len(word) < 5:
#     word.extend(['0'] * (5 - len(words)))
# word = ''.join(word)
# print(word)
#
#
# def solution():
#     global cnt
#     global ans
#     if ans == word:
#         print(cnt)
#     if len(ans) == 5:
#         cnt +=1
#         print(ans)
#         return ans
#     for i in range(0, 5):
#         ans.append(i)
#         solution()
#         ans.pop()
#
# solution()


from itertools import product
def solution(word):
    words = []
    for i in range(1,6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()