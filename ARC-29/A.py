n = int(input())
t = [int(input()) for _ in range(n)]

min_t = 1e9
sum_t = sum(t)
for i in range(2 ** n):
    time = 0
    for j in range(n):
        if (i >> j) & 1:
            time += t[j]
    time = max(time, sum_t - time)
    min_t = min(min_t, time)
print(min_t)