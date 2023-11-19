# 1 = 1 li[0] li[0]+6*0
# 2~7 =6 // li[0]+6*1
# 8~19 = 12 // li[1]+6*2
# 20~37 = 18 // li[2] +6*3
# 38~ 61 =24 58이면 5개 //li[4]=li[3] +6*4
n = int(input())
if n==1:
    print(1)
else:
    li = []
    li.append(1)
    i = 0
    while True:
        li.append(li[i]+6*(i+1))
        if li[i+1]>= n:
            break
        i+=1
    print(i+2)

#TODO 클린 코드
'''
n=int(input())
i=s=1
while s<n:
	s+=6*i
	i+=1
print(i)
'''