# -*- coding: utf-8 -*-
# 整数の入力

A,B = map(int, input().split())

if A%2 != B%2:
	print('IMPOSSIBLE')

else:
	K = (A+B)//2
	print(K)