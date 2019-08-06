# -*- coding: utf-8 -*-
import math
N,D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        diff = 0
        for k in range(D):
            diff += (X[i][k] - X[j][k]) ** 2
        if math.sqrt(diff).is_integer():
            cnt += 1

print(cnt)