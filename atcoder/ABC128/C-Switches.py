# -*- coding: utf-8 -*-
N, M=map(int, input().split())
ks=[]
for _ in range(M):
    k,*s=input().split()
    ks.append((k, list(map(int, s))))
P=list(map(int, input().split()))

#print(ks)

def judge():
	ans=0
	for switches in range(0, 2**N):
		b=bin(switches)[2:].zfill(N)
		#print(b)

		for i in range(M):
			s=ks[i][1]
			p=P[i]
			on=0
			#print(s)



			for j in s:
				#print(j)
				#print(b[j - 1])

				if b[j-1]=="1":
					on+=1

			if on%2!=p:
				break

		else:
			ans+=1
	return ans
 
print(judge())