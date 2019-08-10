# -*- coding: utf-8 -*-
W, H, x, y = map(int, input().split())
Amax = W * H / 2
judge = 0

if x == W / 2 and y == H / 2:
	judge = 1

print(Amax, judge)