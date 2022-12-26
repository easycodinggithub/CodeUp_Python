a, b, c, d = map(int, input().split())
s = a
for i in range(d - 1):
    s *= b
    s += c
print(s)