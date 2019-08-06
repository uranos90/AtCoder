# -*- coding: utf-8 -*-
N = int(input())
A = [int(input()) for i in range(N)]
Am = max(A)
Asm = sorted(A)[-2]

for i in range(N):
	if A[i] != Am:
		print(Am)
	else:
		print(Asm)