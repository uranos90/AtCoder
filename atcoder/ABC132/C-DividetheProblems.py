# -*- coding: utf-8 -*-
N = int(input())
d = list(map(int, input().split()))
ans = 0

d = sorted(d)
ans = d[N // 2] - d[(N // 2) - 1]
print(ans)