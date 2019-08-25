N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
px = [list(map(int, input().split())) for _ in range(Q)]
k = [[0]] * (N - 1)


for n in range(1, N + 1):
	for i in range(N - 1):
		ab[i].sort()

		if n in ab[i]:
			k[i].append(ab[i][0])

print(k)