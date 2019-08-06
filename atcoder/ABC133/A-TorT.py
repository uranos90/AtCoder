# -*- coding: utf-8 -*-
A = list(map(int,input().split()))
ans = A[0]*A[1]

if A[0]*A[1] > A[2]:
	ans = A[2]

print(ans)