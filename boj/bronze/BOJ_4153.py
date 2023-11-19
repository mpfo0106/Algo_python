import sys
lines = sys.stdin.readlines()
for line in lines:
    li = list(map(int,line.split()))
    li.sort()
    if li[0] != 0:
        if li[0] ** 2 + li[1] ** 2 == li[2] ** 2:
            print('right')
        else:
            print('wrong')
    else:
        pass


#TODO 리스트로 받아서 remove로 max를 지우는 방법
# while True:
#     num = list(map(int,input().split()))
#     max_num = max(num)
#
#     if max_num ==0:
#         break
#     
#     num.remove(max_num)
#     if max_num**2==num[0]**2+num[1]**2:
#             print("right")
#     else:
#         print("wrong")
