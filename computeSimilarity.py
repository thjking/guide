# -*- coding:UTF-8 -*-
from math import sqrt

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