# -*- coding: utf-8 -*-
N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

Ld = []
Rd = []

for i in range(M):
	Ld.append(LR[i][0])
	Rd.append(LR[i][1])

if max(Ld) <= min(Rd):
	print(min(Rd) - max(Ld) + 1)
else:
	print(0)