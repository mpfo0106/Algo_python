t = int(input())
for i in range(t):
    h,w,n =map(int,input().split())
    dong = n%h
    ho = int(n/h) +1
    if dong ==0:
        dong = h
        ho -=1
    print(dong,end='')
    if ho<10:
        print(0,end='')
    print(ho)
