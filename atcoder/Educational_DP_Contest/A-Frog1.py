# -*- coding: utf-8 -*-
N = int(input())
h = list(map(int, input().split()))

dp = [0] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for n in range(2, N):
	#print(dp)
	dp[n] += min(abs(h[n] - h[n - 2]) + dp[n - 2], \
		abs(h[n] - h[n - 1]) + dp[n - 1])

#print(dp)
print(dp[N - 1])