for i in range(1, 11):  # 테스트 케이스 10개
    N = int(input())
    heights = list(map(int, input().split()))
    house = 0

    for idx in range(2, N - 2):
        max_height = max(heights[idx - 2], heights[idx - 1], heights[idx + 1], heights[idx + 2])
        capa = heights[idx] - max_height
        if capa > 0:
            house += capa
    print(f'#{i} {house}')
