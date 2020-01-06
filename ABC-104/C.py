d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

min_count = 1001
for i in range(2 ** d):
    s = 0
    count = 0
    max_flag = 0
    for j in range(d):
        if (i >> j) & 1:
            s += 100 * (d - j) * pc[d - j - 1][0] + pc[d - j - 1][1]
            count += pc[d - j - 1][0]
        elif max_flag == 0:
            max_flag = d - j

        if s >= g:
            min_count = min(min_count, count)
            s = 0
            count = 0
            break

    for _ in range(pc[max_flag - 1][0]):
        s += 100 * max_flag
        count += 1
        if s >= g:
            min_count = min(min_count, count)
            s = 0
            count = 0
            break

print(min_count)