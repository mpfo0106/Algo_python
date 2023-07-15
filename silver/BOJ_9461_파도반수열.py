arr = [0]*101
arr[1] = arr[2] = arr[3] =1
arr[4]= arr[5] = 2

cur = 1

for i in range(6,101):
        arr[i] = arr[i-1]+ arr[cur]
        cur+=1
t = int(input())
for _ in range(t):
    n = int(input())
    print(arr[n])
