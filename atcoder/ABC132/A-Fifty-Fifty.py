# -*- coding: utf-8 -*-
S = input()
S = [str(c) for c in S]

cnt = 0

for i in range(4):
	cnt += S.count(S[i])
	
if cnt == 8:
	print('Yes')
else:
	print('No')