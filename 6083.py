r, b, g = map(int, input().split())
s = 0
for i in range(0, r):
    for j in range(0, b):
        for k in range(0, g):
            print(i, j, k)
            s += 1
print(s)