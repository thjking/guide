# -*- coding:UTF-8 -*-
from math import sqrt

# 皮尔逊相关系数函数
def pearson(rating1,rating2):
	n = 0
	a = 0
	b1 = 0
	b2 = 0
	b = 0
	c1 = 0
	c = 0
	d1 = 0
	d = 0
	r = 0
	for key in rating1:
		if key in rating2:
			n += 1
			a += rating1[key] * rating2[key]
			b1 += rating1[key]
			b2 += rating2[key]
			c1 += pow(rating1[key],2)
			d1 += pow(rating2[key],2)
	b =(b1 * b2) / n
	c = sqrt(c1 - pow(b1,2) / n)
	d = sqrt(d1 - pow(b2,2) / n)
	if c * d == 0:
		return 0
	else:
		r = (a - b) / (c * d)
		return r
# print pearson(users['Angelica'],users['Hailey'])


# 利用皮尔逊相关系数进行相似度递增排序
def computeNearestNeighbor_Pea(username,users):
	distances = []
	for user in users:
		if user != username:
			distance = pearson(users[username],users[user])
			distances.append((distance,user))
	distances.sort()
	return distances
# print computeNearestNeighbor_Pea('Hailey',users)