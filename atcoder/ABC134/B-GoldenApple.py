# -*- coding:utf-8 -*-
A = list(map(int,input().split()))

judge = 0
remain = A[0]

for i in range(A[0]):
	remain -= 2*A[1] + 1
	if remain <= 0:
		judge = i + 1 
		break
print(judge)