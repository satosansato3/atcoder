n, m = map(int, input().split())
xy = set()
for _ in range(m):
    xy.add(tuple(map(int, input().split())))

c = 0
for i in range(2 ** n):
    g = []
    for j in range(n):
        if (i >> j) & 1:
            g.append(j+1)
    flag = 0
    for k in range(len(g)):
        for l in range(len(g) - k - 1):
            if (g[k], g[k+l+1]) not in xy:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        c = max(c, len(g))
print(c)

