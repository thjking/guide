# -*- coding:UTF-8 -*-
from math import sqrt
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

users3 = {"David":{"Imagine Dragons":3,"Daft Punk":5,
					"Lorde":4,"Fall Out Boy":1},
		  "Matt":{"Imagine Dragons":3,"Daft Punk":4,
		            "Lorde":4,"Fall Out Boy":1},
		  "Ben":{"Kacey Musgraves":4,"Imagine Dragons":3,
		          "Lorde":3,"Fall Out Boy":1},
		  "Chris":{"Kacey Musgraves":4,"Imagine Dragons":4,
		            "Daft Punk":4,"Lorde":3,"Fall Out Boy":1},
	      "Tori":{"Kacey Musgraves":5,"Imagine Dragons":4,
		            "Daft Punk":5,"Fall Out Boy":3}
}
# users3的物品列表
content = ["Imagine Dragons","Daft Punk","Fall Out Boy","Lorde","Kacey Musgraves"]
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

#利用改进版余弦相似度求物品间相似程度
def computeSimilarity(band1,band2,userRatings):
	average = {}
	similarity = {}
	for (key,rat) in userRatings.items():
		average[key] = (float(sum(rat.values()))
		                /len(rat.values()))
	num = 0
	num1 = 0
	num2 = 0
	for (user,rat) in userRatings.items():
		if band1 in rat and band2 in rat:
			num += ((rat[band1] - average[user])*(rat[band2] - average[user]))
			num1 += pow((rat[band1] - average[user]),2)
			num2 += pow((rat[band2] - average[user]),2)
	if sqrt(num1) * sqrt(num2) == 0:
		return 0
	else:
		similarity[band1+','+band2] = float(num / (sqrt(num1) * sqrt(num2)))
		return similarity
		#print band1,',',band2,'----',float(num / (sqrt(num1) * sqrt(num2)))

computeSimilarity(content[0],content[1],users3)

def computeSimilarity_all(content):
	similarity = {}
	n = len(content)
	for i in range(0,n):
		for j in range(0,n):
			if i != j:
				#computeSimilarity(content[i],content[j],users3)
				similarity.update(computeSimilarity(content[i],content[j],users3))
	return similarity
print computeSimilarity_all(content)