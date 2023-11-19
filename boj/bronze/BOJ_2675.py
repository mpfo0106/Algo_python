import sys
n = int(sys.stdin.readline())
for i in range(n):
    newLine = ''
    line = sys.stdin.readline().split()
    word = list(line[1].strip())
    for j in word:
        newLine += j * int(line[0])
    print(newLine)