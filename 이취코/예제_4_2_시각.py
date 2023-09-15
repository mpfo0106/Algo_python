# n = int(input())
# cnt =0
# for i in range(60):
#     minute =str(i).split()
#     if minute[0] ==3 or minute[1] ==3:
#         cnt+=1
#         cnt+=60
#         continue
#     for j in range(60):
#         sec = str(i).split()
#         if sec[0] == 3 or sec[1] == 3:
#             cnt += 1
# one_hour_cnt = cnt
#
# if n//3>0:
#     tmp = (n//3)* one_hour_cnt+ (60*60)
# if n%3 >0:
#     tmp += one_hour_cnt* (n%3)
h = int(input())
cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or str(j) or str(k):
                cnt +=1
print(cnt)
