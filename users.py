# -*- coding:UTF-8 -*-
import math
users = {
"Angelica":{"Blue Traveler":3.5,"Broken Bells":2.0,
"Norah Jones":4.5,"Phoenix":5.0,"Slightly Stoopid":1.5,
"The Strokes":2.5,"Vampire Weekend":2.0},

"Bill":{"Blue Traveler":2.0,"Broken Bells":3.5,
"Deadmau5":4.0,"Phoenix":2.0,"Slightly Stoopid":3.5,
"Vampire Weekend":3.0},

"Chan":{"Blue Traveler":5.0,"Broken Bells":1.0,
"Deadmau5":1.0,"Norah Jones":3.0,"Phoenix":5.0,
"Slightly Stoopid":1.0},

"Dan":{"Blue Traveler":3.0,"Broken Bells":4.0,
"Deadmau5":4.5,"Phoenix":3.0,"Slightly Stoopid":4.5,
"The Strokes":4.0,"Vampire Weekend":2.0},

"Hailey":{"Broken Bells":4.0,"Deadmau5":1.0,
"Norah Jones":4.0,"The Strokes":4.0,"Vampire Weekend":1.0},

"Jordyn":{"Broken Bells":4.5,"Deadmau5":4.0,
"Norah Jones":5.0,"Phoenix":5.0,"Slightly Stoopid":4.5,
"The Strokes":4.0,"Vampire Weekend":4.0},

"Sam":{"Blue Traveler":5.0,"Broken Bells":2.0,
"Norah Jones":3.0,"Phoenix":5.0,"Slightly Stoopid":4.0,
"The Strokes":5.0},

"Veronica":{"Blue Traveler":3.0,"Norah Jones":5.0,
"Phoenix":4.0,"Slightly Stoopid":2.5,
"The Strokes":3.0},

}

# print users["Veronica"]

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

# 欧式距离计算函数
def Minkowski(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += pow((rating1[key]-rating2[key]),2)
	distance = math.sqrt(distance)
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
	c = math.sqrt(c1 - pow(b1,2) / n)
	d = math.sqrt(d1 - pow(b2,2) / n)
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