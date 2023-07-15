import sys
nums =[]
noDup = set([]) #중복 제거용 set 하나 설정
for i in range(10):
    nums.append(int(sys.stdin.readline().strip()))
for num in nums:
    noDup.add(num%42)
print(len(noDup)) #set 의 길이

#TODO 나처럼 안하고 바로 입력받으면서 set 넣기

l = []
for i in range(10):
    A = int(input())
    n = A%42
    l.append(n)
l = list(set(l))
print(len(l))