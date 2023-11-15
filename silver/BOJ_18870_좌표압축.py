import sys

N = sys.stdin.readline()
ogLines = list(map(int, sys.stdin.readline().strip().split(" ")))
newLines = set(ogLines)
sortedLines = sorted(newLines)

mapping = {}
answer = []
for i, sortedLine in enumerate(sortedLines):
    mapping[sortedLine] = i

for ogLine in ogLines:
    answer.append(mapping[ogLine])
answer = map(str, answer)
print(' '.join(answer))
