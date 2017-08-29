# -*- coding:UTF-8 -*-
from math import sqrt

# 欧式距离计算函数
def Minkowski(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += pow((rating1[key]-rating2[key]),2)
	distance = sqrt(distance)
	return distance
	
# print Minkowski(users["Bill"],users["Hailey"])

# 利用欧式函数进行相似度递增排序
def computeNearestNeighbor_Min(username,users):
	distances = []
	for user in users:
		if user != username:
			distance = Minkowski(users[username],users[user])
			distances.append((distance,user))
	distances.sort()
	return distances
# print computeNearestNeighbor_Min('Hailey',users)