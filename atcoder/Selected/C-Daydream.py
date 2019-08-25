# -*- codNng: utf-8 -*-
S = input()
T = ""
i = len(S)

while i > 0:
	if S[i-5:i] == 'dream':
		i = i - 5
		T = 'dream' + T

	elif S[i-5:i] == 'erase':
		i = i - 5
		T = 'erase' + T

	elif S[i-7:i] == 'dreamer':
		i = i - 7
		T = 'dreamer' + T

	elif S[i-6:i] == 'eraser':
		i = i - 6
		T = 'eraser' + T

	else:
		break


if S == T:
	print('YES')
 
else:
	print('NO')