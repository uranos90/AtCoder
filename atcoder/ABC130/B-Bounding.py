# -*- coding: utf-8 -*-
N, X = map(int, input().split())
L = list(map(int, input().split()))
D = [0] * 1 
Dtemp = 0

for i in range(0, N):
	Dtemp = D[i] + L[i]
	if len(D) > N + 1:
		print(N + 1)
		exit()
	elif Dtemp > X:
		print(len(D))
		exit()
	else:
		D.append(Dtemp)

print(len(D))