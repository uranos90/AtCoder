import bisect

n, m = map(int, input().split())
s = [int(input()) for _ in range(n)]
s += [0]
s = sorted(s)
t = set()
for i in s:
    for j in s:
        t.add(i + j)

t = list(t)
t = sorted(t)
ans = 0

for i in t:
    k = m - i
    idx = bisect.bisect_left(t, k)
    if t[idx - 1] + i <= m:
        ans = max(ans, t[idx - 1] + i)
    if 0 <= idx < len(t) and t[idx] + i <= m:
        ans = max(ans, t[idx] + i)

print(ans)
