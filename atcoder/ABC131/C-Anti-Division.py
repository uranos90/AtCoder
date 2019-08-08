# -*- coding: utf-8 -*-
A, B, C, D = map(int, input().split())
ans = 0
Am = 0
Bm = 0
df = 0
t = 0

def lcm(x, y):
	return (x * y) // gcd(x, y)

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

t = B - A + 1
Am = (A - 1) // C + (A - 1) // D - (A - 1)//lcm(C, D)
Bm = B // C + B // D - B // lcm(C, D)
ans = t - (Bm - Am)

print(ans)