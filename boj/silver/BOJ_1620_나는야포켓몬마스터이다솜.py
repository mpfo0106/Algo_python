import sys
n, m = map(int,sys.stdin.readline().strip().split())
poket_index = {}
poket_name = {}
ans = []
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    poket_index[i] = name
    poket_name[name] = i
for i in range(m):
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit(): #숫자로 물어봤으면
        ans.append(poket_index[int(quiz)]+'\n')
    else: # 이름으로 물어봤으면
        ans.append(str(poket_name[quiz])+'\n')
print(''.join(ans))