# -*- coding: utf-8 -*-

N = int(input())
p = list(map(int,input().split()))
#print(p[0])
flag = 0

for i in range(N):	
	if p[i] != i + 1 : #iは０からはじまるから＋１する
		flag = flag + 1

if flag <= 2:
	print("YES")
else:
	print("NO")