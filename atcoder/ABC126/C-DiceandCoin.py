# -*- coding: utf-8 -*-
import math
N, K = map(int, input().split())
ans = 0

if N >= K - 1:
	ans = (N - K + 1) * (1 / N)

	for i in range(1, K):
		j = math.floor((math.log2((K - 1) / i)) + 1)
		ans += (1 / N) * (1 / 2) ** j

else:
	for i in range(1, N + 1):
		j = math.floor((math.log2((K - 1) / i)) + 1)
		ans += (1 / N) * (1 / 2) ** j

print(ans)