# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()

Ali = 0
Bob = 0

for i in range(0, N, 2):
	Ali += a[i]

for j in range(1, N, 2):
	Bob += a[j]

print(abs(Ali - Bob))