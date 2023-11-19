import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    name, score =sys.stdin.readline().split()
    array.append((int(score),name))
array.sort(key=lambda student : student[1])

for student in array:
    print(student[1],end=" ")
