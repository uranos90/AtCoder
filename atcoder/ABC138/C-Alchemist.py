# -*- coding: utf-8 -*-
N = int(input())
v = list(map(int, input().split()))
tmp = 0
v.sort()

tmp = (v[0] + v[1]) / 2

for i in range(2, N):
	tmp = (tmp + v[i]) / 2

print(tmp)