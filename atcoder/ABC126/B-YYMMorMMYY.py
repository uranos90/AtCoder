# -*- coding: utf-8 -*-
S = list(input())
FF = ''
RR = ''
J = [0] * 2

for st in S[0],S[1]:
	FF += st

for st in S[2],S[3]:
	RR += st

if 1 <= int(FF) <= 12:
	J[0] = 1
else:
	J[0] = 0

if 1 <= int(RR) <= 12:
	J[1] = 1
else:
	J[1] = 0

if J[0] == 0 and J[1] == 0:
	print('NA')
elif J[0] == 0 and J[1] == 1:
	print('YYMM')
elif J[0] == 1 and J[1] == 0:
	print('MMYY')
else:
	print('AMBIGUOUS')