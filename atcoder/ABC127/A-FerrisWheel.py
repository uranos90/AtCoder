# -*- coding: utf-8 -*-
A, B = map(int, input().split())

if A >= 13:
	ans = B
elif 6 <= A <= 12:
	ans = B // 2
else:
	ans = 0

print(ans)