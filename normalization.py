# -*- coding:UTF-8 -*-
from math import sqrt

# 归一化之缩小函数（字典形式）
def narrow_dic(min,max,users):
	for (key,rat) in users.items():
		for key in rat:
			rat[key] = float(2 * (rat[key] - min) - (max - min)) / (max - min)
	return users
# print narrow_dic(1,5,users3)

# 归一化之缩小函数（数值形式）
def narrow_num(min,max,num):
	return float(2 * (num - min) - (max - min)) / (max - min)
# print narrow)_num(1,5,3)

# 归一化之放大函数（字典形式）
def enlarge_dic(min,max,users):
	for (key,rat) in users.items():
		for key in rat:
			rat[key] = float((rat[key] + 1)) / 2 * (max - min) + min
	return users
	
# 归一化之放大函数（数值形式）
def enlarge_num(min,max,num):
	return float((num + 1)) / 2 * (max - min) + min