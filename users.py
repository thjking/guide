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

users2 = {"Amy":{"Taylor Swift":4,"PSY":3,"Whitney Houston":4},
		  "Ben":{"Taylor Swift":5,"PSY":2},
		  "Clara":{"PSY":3.5,"Whitney Houston":4},
		  "Daisy":{"Taylor Swift":5,"Whitney Houston":3}}

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

# 利用改进版余弦相似度求物品间相似程度(数值形式)
def computeSimilarity_num(band1,band2,userRatings):
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
		return float(num) / (sqrt(num1) * sqrt(num2))
# computeSimilarity(content[2],content[4],users3)

# 利用改进版余弦相似度求物品间相似程度(字典形式)
def computeSimilarity_dic(band1,band2,userRatings):
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
		similarity[band1+','+band2] = float(num) / (sqrt(num1) * sqrt(num2))
		return similarity
# computeSimilarity(content[2],content[4],users3)

# 计算任意两物品之间相似度函数（字典形式）
def computeSimilarity_all(content):
	similarity = {}
	n = len(content)
	for i in range(0,n):
		for j in range(0,n):
			if i != j:
				#需搭配字典形式computeSimilarity()函数使用
				similarity.update(computeSimilarity(content[i],content[j],users3))
	return similarity
# print computeSimilarity_all(content)

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

# 基于物品相似度的评分预测函数(字典形式)
def predict_dic(user,content,users,min,max):
	sum1 = 0
	sum2 = 0
	dict = {}
	users = narrow_dic(min,max,users)
	user_s = users[user]
	for key in user_s:
		sum1 += user_s[key] * computeSimilarity(key,content,users)
		sum2 += abs(computeSimilarity(key,content,users))
	dict[user+','+content] = float(sum1) / sum2
	return dict
	
# 基于物品相似度的评分预测函数(数值形式)
def predict_num(user,content,users,min,max):
	sum1 = 0
	sum2 = 0
	dict = {}
	users = narrow_dic(min,max,users)
	user_s = users[user]
	for key in user_s:
		sum1 += user_s[key] * computeSimilarity(key,content,users)
		sum2 += abs(computeSimilarity(key,content,users))
	return float(sum1) / sum2

# 以上数函数待加入数值形式以适应不同计算

def dev(i,j,users):
	num = 0
	sum = 0
	for(key,rat) in users.items():
		if i in rat and j in rat:
			num += 1
	for(key,rat) in users.items():
		if i in rat and j in rat:
			sum += float(rat[i] - rat[j]) / num
	return sum
print dev('Whitney Houston','PSY',users2)

def computeDeviations(user):
    frequemcies = {}    #用户评价数字典
    deviations = {}     #评分偏差累计字典    
    for ratings in user.values():
        for(item,rat) in ratings.items():
            frequemcies.setdefault(item,{})    #加入用户评价数字典的键与初始化键值字典
            deviations.setdefault(item,{})     #同上
            for(item2,rat2) in ratings.items():     
                if item != item2:
                    frequemcies[item].setdefault(item2,0)    #加入键值字典的键与键值
                    deviations[item].setdefault(item2,0.0)   #同上
                    frequemcies[item][item2] += 1            #计算评分人数
                    deviations[item][item2] += rat - rat2    #累加评分偏差
    for (item,rat) in deviations.items():
        for item2 in rat:
            rat[item2] /= frequemcies[item][item2]    #评分偏差/评分人数
    return deviations                                 #返回更新后评分偏差字典
print computeDeviations(users2)