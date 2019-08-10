# -*- coding: utf-8 -*-
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] * N
dp[0] = 0
temp = [10**4] * K


for n in range(1, N):
	#print(dp)
	if n < K:
		for k in range(n):
			temp[k] = dp[k] + abs(h[n] - h[k])
			
	else:
		for k in range(K):
			temp[k] = dp[n - k - 1] + abs(h[n] - h[n - k - 1])
	dp[n] = min(temp)
	#print(temp)

#print(dp)
print(dp[N - 1])