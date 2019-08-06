# -*- coding: utf-8 -*-

N = input()
K = int(len(N))
A = 0

if K % 2 == 0:
	for i in range(0,K,2):
		A += 9 * 10 ** i
elif K == 1:
	A = N
else:
	for i in range(0,K - 1,2):
		A += 9 * 10 ** i

if K % 2 != 0 and K != 1:
	A += int(N) - 10**(K - 1) + 1

print(A)