# -*- coding: utf-8 -*-
N,L = map(int, input().split())
A = []
ans = 0

for i in range(1, N + 1):
	A.append(L + i - 1)

if A[0] > 0:
	for j in range(1, N):
		ans += A[j]

elif A[N - 1] < 0:
	for j in range(0, N - 1):
		ans += A[j]

else:
	for j in range(N):
		ans += A[j]
print(ans)