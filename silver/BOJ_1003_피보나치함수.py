def fibonacci(c,ans):
    for n in range(c):
        if n == 0:
            ans[0]+=1
            return 0
        elif n==1:
            ans[1]+=1
            return 1
        else:
            return fibonacci(n-1,ans)+fibonacci(n-2,ans)

t=int(input())
for i in range(t):
    n = int(input())
    ans = [0]*2
    fibonacci(n,ans)
    print(str(ans[0])+" "+ str(ans[1]))


