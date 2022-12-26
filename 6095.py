d = [[0 for j in range(20)] for i in range(20)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    d[a-1][b-1] = 1
for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print('')