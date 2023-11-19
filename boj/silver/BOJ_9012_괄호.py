import sys
n = int(sys.stdin.readline())
for i in range(n):
    stk = []
    li = list(sys.stdin.readline().strip())
    for l in li:
        stk.append(l)
        if len(stk)>1:
            if stk[-1] ==')' and stk[-2] == '(':
                del stk[-2:]
    if len(stk)==0:
        print('YES')
    else:
        print("NO")
#TODO 굳이 두개 다 받을 필요없이 (이 아니면 del 시켜버리기
'''
if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
                
'''
