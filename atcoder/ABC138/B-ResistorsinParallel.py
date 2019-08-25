# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
P = 0

for i in range(N):
	P += 1 / A[i]

print(1/P)