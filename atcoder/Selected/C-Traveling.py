# -*- codNng: utf-8 -*-
N = int(input())
tx = []
xt = 0
yt = 0
d = 0
td = 0
tt = 0

for _ in range(N):
    t,*x=map(int, input().split())
    tx.append((t, list(map(int, x))))

for i in range(N):
	d = abs(tx[i][1][0] - xt) + abs(tx[i][1][1] - yt)
	td = tx[i][0] - tt
	
	#print(d)
	#print(td)

	if td % d == 0:
		xt = tx[i][1][0]
		yt = tx[i][1][1]
		tt = tx[i][0]
	
	else:
		print('No')
		exit()

print('Yes')