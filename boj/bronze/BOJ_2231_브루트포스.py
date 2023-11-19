n = input()
li = list(map(int,n))
i = 0
if int(n)>18:
    start = int(n) - 9*len(li)
else:
    start = 0
end = int(n)
while True:
    if start < end:
        startList = list(map(int,str(start)))
        rem = sum(startList)
        if int(n) == start+rem:
            print(start)
            break
        else:
            start+=1
    else:
        print(0)
        break

""" 
리스트에 넣어서 len얻지 말고
그냥 len(n) 해서 얻어도돼. input은 str 형이니까

while 말고 range(start,int(n)) 쓰는것도 굳

리스트 안쓰고 그냥 str 타입으로 for 를 돌리기
ex) str_num = str(i) , sum = i 
    for j in str_num:
        sum += int(j)


----------------------
N = input()

start = 0
if len(N) > 3:
    start = int(N) - len(N) * 9
for i in range(start, int(N)):
    str_num = str(i)
    sum = i
    for j in str_num:
        sum += int(j)
    if sum == int(N):
        print(i)
        break
else:
    print(0)

"""
