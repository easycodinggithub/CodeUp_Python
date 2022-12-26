h, b, c = map(int, input().split())
s = h*b*c/8/1024/1024
ss = round(s, 2)
print(format(float(ss), ".2f"), 'MB')