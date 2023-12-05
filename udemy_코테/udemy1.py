# 직사각형을 만드는 나머지 한점의 좌표
# 점 3개 좌표가 매개변수로
# x축 y 축에 평행
# x축이 같은게 두개 나오면 나머지 하나는 다른 x축
# y축이 같은게 두개나오면 나머지 하나는 다른 y축
def solution(v):
    spot_x = {}
    spot_y = {}
    for spot in v:
        x,y = spot
        if x in spot_x:
            spot_x[x] += 1
        else:
            spot_x[x] = 1
        if y in spot_y:
            spot_y[y] += 1
        else:
            spot_y[y] = 1

    answer_x = [spot for spot, count in spot_x.items() if count ==1]
    answer_y = [spot for spot, count in spot_y.items() if count ==1]
    answer = answer_x+answer_y

    return answer


v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))

def solution(v):
    spot_x = {}
    spot_y = {}
    for spot in v:
        x,y = spot
        if x in spot_x:
            spot_x[x] +=1
        else:
            spot_x[x] =1

    answer_x = [spot for spot,count in spot_x.items()]