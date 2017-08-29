# -*- coding:UTF-8 -*-
from math import sqrt

# 曼哈顿距离计算函数
def manhattan(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance
	
# print manhattan(users['Hailey'],users['Jordyn'])

# 利用曼哈顿函数进行相似度递增排序
def computeNearestNeighbor_Man(username,users):
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[username],users[user])
			distances.append((distance,user))
	distances.sort()
	return distances

# print computeNearestNeighbor_Man('Hailey',users)