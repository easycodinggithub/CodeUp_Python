a, b, c = map(int, input().split())
s = a
for i in range(c - 1):
    s *= b
print(s)