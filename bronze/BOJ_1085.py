#0,0 과 w,h 를 나눈 값중에 x y가 가까운 쪽으로 붙는다
# 0+w /2 < x 면 w 쪽 반대면 0쪽= > w-x 값과 ?-y쪽 결과값 비교해서 더 작은쪽으로
x,y,w,h = map(int,input().split())
d1 = x
d2 = y
if w/2 <x:
    d1 = w-x
if h/2 <y:
    d2 = h-y
print(min(d1,d2))
#TODO print(min(x,y,(w-x),(h-y)))