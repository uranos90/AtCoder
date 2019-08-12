# -*- coding: utf-8 -*-
N = int(input())
dic = {}
cnt = 0

for i in range(N):
	s = str(sorted(input()))
	if (s in dic):
		cnt += dic[s]
		dic[s] += 1
	else:
		dic[s] = 1

print(cnt)