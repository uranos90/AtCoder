# -*- coding: utf-8 -*-
# 整数の入力
print('input number')
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{},{},{}".format(a+b+c, s, a/b))