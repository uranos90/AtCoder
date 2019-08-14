# -*- coding: utf-8 -*-
N = int(input())
tmp = []
ans = []

for i in range(N):
	a, b = input().split()
	tmp.append(list((i + 1, a, int(b))))
	
ans = sorted(tmp, key = lambda x:(x[1], -x[2]))

for i in range(N):
	print(ans[i][0])