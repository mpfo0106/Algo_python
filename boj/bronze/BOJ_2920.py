n=list(input().split())
ascList = sorted(n) #정렬 하면 원본도 변경되서 sorted 를 사용해줘야해
desList = sorted(n,reverse=True) #리버스 정렬된 리스트
if ascList == n:
    print('ascending')
elif desList == n:
    print('descending')
else:
    print('mixed')