# -*- coding: utf-8 -*-
N, M=map(int, input().split())
ks=[]
for _ in range(M):
    k,*s=input().split()
    ks.append((k, list(map(int, s))))
P=list(map(int, input().split()))
ans = 0

for i in range(2**N):
	Nb = format(i, 'b')
	Nb = Nb.zfill(N)
	
	for j in range(M):
		s = ks[j][1]
		on = 0

		for k in s:			
			if Nb[k - 1] == '1':
				on += 1

		if on % 2 != P[j]:
			break

	else:
		ans += 1
print(ans)