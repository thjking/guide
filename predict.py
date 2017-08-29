# -*- coding:UTF-8 -*-
from math import sqrt
import computeSimilarity as cp
import normalization as nm

# 基于物品相似度的评分预测函数(字典形式)
def predict_dic(user,content,users,min,max):
	sum1 = 0
	sum2 = 0
	dict = {}
	users = nm.narrow_dic(min,max,users)
	user_s = users[user]
	for key in user_s:
		sum1 += user_s[key] * cp.computeSimilarity_num(key,content,users)
		sum2 += abs(cp.computeSimilarity_num(key,content,users))
	dict[user+','+content] = float(sum1) / sum2
	return dict
	
# 基于物品相似度的评分预测函数(数值形式)
def predict_num(user,content,users,min,max):
	sum1 = 0
	sum2 = 0
	dict = {}
	users = nm.narrow_dic(min,max,users)
	user_s = users[user]
	for key in user_s:
		sum1 += user_s[key] * cp.computeSimilarity_num(key,content,users)
		sum2 += abs(cp.computeSimilarity_num(key,content,users))
	return float(sum1) / sum2
