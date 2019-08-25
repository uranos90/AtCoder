# -*- coding: utf-8 -*-
N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**9 + 7

inner = 0
outer = 0
cnt = 0


for i in range(N - 1):
	for k in range(i, N - 1):
		if A[k] > A[k + 1]:
			inner += 1

print(inner)


if A[0] < A[-1]:
	outer = 1


for j in range(1, K + 1):
	cnt += inner * j + outer *(j-1)

print(cnt%INF)