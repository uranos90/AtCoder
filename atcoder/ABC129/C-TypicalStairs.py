N ,M = map(int, input().split())
X = [int(input()) for _ in range(M)]
S = [0] * (N + 1)
dp = [0] * (N + 1)
mod = int(1e9 + 7)

for i in range(M):
	S[X[i]] = -1


for i in range(0, len(X) - 1):
	if X[i + 1] - X[i] == 1:
		print('0')
		exit()

dp[0] = 1
if S[1] != -1: dp[1] = 1

for i in range(2, N + 1):
	#print(dp)
	if S[i - 1] != -1: dp[i] += dp[i - 1]
	if S[i - 2] != -1: dp[i] += dp[i - 2]
	dp[i] %= mod

#print(dp)
print(dp[N])