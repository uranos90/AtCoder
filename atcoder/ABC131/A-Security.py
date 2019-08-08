# -*- coding: utf-8 -*-
S = input()
S = [c for c in S]

for i in range(0,len(S) - 1):
	if S[i] == S[i + 1]:
		print('Bad')
		exit()
print('Good')
