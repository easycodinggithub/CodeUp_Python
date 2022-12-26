h, w = map(int, input().split())
n = int(input())
m = [[0] * w for _ in range(h)]
for k in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        # 가로
        for i in range(0, l):
            m[x - 1][y - 1 + i] = 1
    else:
        # 세로
        for i in range(0, l):
            m[x - 1 + i][y - 1] = 1
for i in range(0, h):
    for j in range(0, w):
        print(m[i][j], end=' ')
    print(end='\n')