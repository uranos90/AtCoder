# -*- coding: utf-8 -*-
N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = 10 ** 9 + 7

inner = 0
outer = 0
cnt = 0
ans = 0

for i in range(N - 1):
    # print(inner)
    for j in range(i, N - 1):
        if A[i] > A[j + 1]:
            inner += 1

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            outer += 1

ans = (inner * K + ((K * (K - 1)) // 2) * outer) % INF
print(ans)
