# -*- coding: utf-8 -*-
import bisect

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.append(0)
L = set()
ans = 0

for i in A:
    for j in A:
        L.add(i + j)

L = sorted(L)

for n in L:
    if M - n > 0:
        idx = bisect.bisect_left(L, M - n)
        if L[idx - 1] + i <= M:
            ans = max(ans, L[idx - 1] + i)

        if 0 <= idx < len(L) and L[idx] + i <= M:
            ans = max(ans, L[idx] + i)

print(ans)
