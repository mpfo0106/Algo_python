# 1 실패
data = input()
count0 = 0 # 전부 0으로
count1 = 0 # 전부 1로

# 첫번째 원소에 대해 처리
if data[0] == '1':
    count0 +=1
else:
    count1 +=1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': # 맨 초기상태가 뭐든간에 순간의 탐욕
            count0 += 1
        else:
            count1 +=1
print(min(count0,count1))
