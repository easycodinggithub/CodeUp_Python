location = []
for i in range(0, 10):
    location.append([])
    for j in range(0, 10):
        location[i].append(0)

for i in range(0, 10):
    location[i] = list(map(int, input().split()))
sy = 1
sx = 1
location[sy][sx] = 9
while True:
    if location[sy][sx+1] == 0:
        sx += 1
        location[sy][sx] = 9
    elif location[sy+1][sx] == 0:
        sy += 1
        location[sy][sx] = 9
    elif location[sy][sx+1] == 2:
        sx += 1
        location[sy][sx] = 9
        break
    elif location[sy+1][sx] == 2:
        sy += 1
        location[sy][sx] = 9
        break
    else:
        break

for i in range(0, 10):
    for j in range(0, 10):
        print(location[i][j], end=" ")
    print(end='\n')

