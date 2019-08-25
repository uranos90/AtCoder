# -*- coding: utf-8 -*-
N, A, B = map(int, input().split())
cnt = 0

for i in range(1, N + 1):
	S = [int(c) for c in str(i)]
	
	for j in range(A, B + 1):
		if sum(S) == j:
			cnt += i

print(cnt)