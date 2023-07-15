n = input()
people = list(map(int,input().split()))
people.sort()
time = 0
for i in range(n):
    time += people[i] * (n-i)
print(time)