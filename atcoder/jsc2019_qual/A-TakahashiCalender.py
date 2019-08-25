# -*- coding: utf-8 -*-
M, D = map(int, input().split())
cnt = 0

for i in range(1, M + 1):
	for j in range(1, D + 1):
		j = str(j).zfill(len(str(D)))

		if int(j[0]) >= 2 and int(j[1]) >=2:

			if int(j[0]) * int(j[1]) == i:
				#print(i,j)
				cnt += 1

print(cnt)