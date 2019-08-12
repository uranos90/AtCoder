# -*- coding: utf-8 -*-
K, X = map(int, input().split())
ans = [0] * (K * 2 - 1)
ans[0] = X - (K - 1)

for i in range(1, len(ans)):
	ans[i] = ans[i - 1] + 1

print(*ans)