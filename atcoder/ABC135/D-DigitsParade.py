S=input()
dp=[[0]*13 for i in range(len(S)+1)]
#print(dp)
mod=10**9+7
dp[0][0]=1
for n in range(len(S)):
    for t in range(13):
        if S[n]!='?':
            dp[n+1][(10*t+ int(S[n]))%13]+=dp[n][t]
            #dp[n + 1][(10 * t + int(S[n])) % 13] %=mod
            #print(dp[n + 1][(10 * t + int(S[n])) % 13])
            #print(dp)
        else:
            for s in range(10):
                dp[n+1][(10*t+ s)%13]+=dp[n][t]
                #dp[n + 1][(10 * t + s) % 13] %= mod
                #print(dp[n + 1][(10 * t + s) % 13])
                #print(dp)
print(dp)
#print(dp[len(S)][5])
