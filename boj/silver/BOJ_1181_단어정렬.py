import sys
# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst) // 2]
#     lesser_lst, equal_lst, greater_lst = [], [], []
#     for num in lst:
#         if len(num) < len(pivot):
#             lesser_lst.append(num)
#         elif len(num) > len(pivot):
#             greater_lst.append(num)
#         else:
#             equal_lst.append(num)
#     return quick_sort(lesser_lst) + equal_lst + quick_sort(greater_lst)

n = int(sys.stdin.readline().strip())
setLst = set([])
for i in range(n):
    setLst.add(sys.stdin.readline().strip())
lst = list(setLst)
lst.sort()
lst.sort(key=lambda x:len(x))
# newLst =quick_sort(lst)

for i in lst:
    print(i)

#TODO 정렬 의 lambda를 사용해서 정렬하자