# -*- coding: utf-8 -*-

A = list(map(int,input().split()))
remain = 0

if A[2] - (A[0] - A[1]) <= 0:
	print(remain)
else:
	remain = A[2] - (A[0] - A[1])
	print(remain)