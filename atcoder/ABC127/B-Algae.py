# -*- coding: utf-8 -*-
r, D, x = map(int, input().split())

for _ in range(10):
	xd = r * x - D
	print(xd)
	x = xd