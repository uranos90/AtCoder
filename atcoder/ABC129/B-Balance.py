# -*- coding: utf-8 -*-
N = int(input())
W = list(map(int, input().split()))
Wtotal = 0
S1 = 0
S2 = 0
Wdf = [0] * N

for i in range(len(W)):
	Wtotal += W[i]

for j in range(len(W)):
	S1 += W[j]
	S2 = Wtotal - S1
	Wdf[j] = abs(S1 - S2)

print(min(Wdf))	