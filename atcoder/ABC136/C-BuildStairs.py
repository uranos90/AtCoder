# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int,input().split()))

ans = 'Yes'
diff = 0

for i in range(N - 1):
	diff = H[i + 1] - H[i]

	if diff >= 1:
		H[i + 1] -= 1
	elif diff < 0:
		ans = 'No'

print(ans)