# -*- coding: utf-8 -*-
 
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = 0
 
for i in range(N):
	if A[i] > B[i]:
	
		M = B[i] + M
	
	elif B[i] > A[i] + A[i+1]:
 
		M = A[i] + A[i+1] + M
		A[i+1] = 0
 
	else:
 
		M = A[i] + min(B[i]-A[i],A[i+1]) + M
		A[i+1] = A[i+1] - (B[i] - A[i])
 
print(M)