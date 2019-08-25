S = input()
dp = [0] * (len(S) + 1)
dp[1] = 1

if S[0] == S[1]:
	dp[2] = 1
else:
	dp[2] = 2

for i in range(3, len(S) + 1):
	if S[i - 1] != S[i - 2]:
		dp[i] = dp[i - 1] + 1
	else:
		dp[i] = dp[i - 3] + 2
	print(dp)

print(dp[-1])