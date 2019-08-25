# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
Ad = [0] * N
tmp = 0

for i in range(N):
	tmp = A[i]
	while True:
		if tmp % 2 == 0:
			Ad[i] += 1
			tmp = tmp / 2
		else:
			tmp = 0
			break
print(min(Ad))