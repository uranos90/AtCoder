# -*- coding: utf-8 -*-
L, R = map(int, input().split())

ans = 2018
tmp = 0

for i in range(L, R):
	for j in range(i + 1, R + 1):
		tmp = (i * j) % 2019

		if tmp == 0:
			ans = tmp
			print(ans)
			exit()
		else:
			ans = min(tmp, ans)

print(ans)