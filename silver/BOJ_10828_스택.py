import sys
n = int(sys.stdin.readline())
class stack():
    def __init__(self):
        self.items = []
    def __len__(self):
        return len(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.empty():#스택이 비어있으면 1이니
            return -1
        return self.items.pop()
    def empty(self):
        if len(self) == 0: #스택이 비어있으면
            return 1
        else:
            return 0
    def top(self):
        if self.empty():
            return -1
        return self.items[-1]

stk = stack()
for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stk.push(int(line[1]))
    elif line[0] == 'pop':
        print(stk.pop())
    elif line[0] == 'size':
        print(stk.__len__())
    elif line[0] == 'empty':
        print(stk.empty())
    elif line[0] == 'top':
        print(stk.top())

#TODO 단어 포함된거 여부 확인할때 in 사용하기 + writeline 사용
'''
if 'push' in command:
        value = int(command.split()[1])
        stack.append(value)

writeline = sys.stdout.write
elif 'empty' in command:
        writeline(str(1 if not stack else 0) + '\n')
'''