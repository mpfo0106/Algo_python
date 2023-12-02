import sys

n = int(sys.stdin.readline())
student = []
for _ in range(n):
    name, score = sys.stdin.readline().split()
    score = int(score)
    student.append((name, score))

student.sort(key=lambda x: x[1])

print(student)