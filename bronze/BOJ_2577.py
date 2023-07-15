import sys
sum = 1
listSum = []
for i in range(3):
    tmp = int(sys.stdin.readline())
    sum *= tmp
dicSum = {}
for i in str(sum):
    listSum.append(i)
for i in listSum:
    try: dicSum[i] +=1 #중복 등장
    except:dicSum[i] = 1 #중복 없을때

for i in range(10):
    i = str(i)
    try: #dic이 있을 경우
        print(dicSum[i])
    except:
        print('0')

#TODO 문자열을 깡으로 그냥 세기
#print(str(3102000200).count(str(0)))