'''
3kg / 5kg
최소 봉지

-1
'''
n = int(input())
a = int(n/5)
flag =1
try:
    for i in range(a+1):
        tmp = n
        kg5 = a-i
        rem = (tmp - 5 * (kg5)) #5키로 가득
        for kg3 in range(int(rem/3)+1):
            if rem - 3*kg3 == 0:
                raise NotImplemented
        if i == a and kg3== int(n/3):
            print(-1)
except:
    print(kg5 + kg3)

'''
깔끔풀이  // 은 몫이다.
n = int (input ())
five = n // 5
while five >= 0 :
    three = (n - 5 * five) // 3
    if (5 * five + 3 * three) == n :
        print (five + three)
        break
    five = five - 1
if five == -1:
    print (-1)
'''

