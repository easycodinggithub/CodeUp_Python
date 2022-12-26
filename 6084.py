h, b, c, s = map(int, input().split())
s = h*b*c*s/8/1024/1024
ss = round(s, 1)
print(format(float(ss), ".1f"), 'MB')