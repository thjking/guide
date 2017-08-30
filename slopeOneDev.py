# -*- coding:UTF-8 -*-
from math import sqrt

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
    return deviations,frequemcies                                 #返回更新后评分偏差字典


def slopeOneRecommendtions(user):
    deviations,frequemcies = computeDeviations(user)
    recommend = {}
    freq = {}
    recommendations = {}
    for key in user:
        for (item,rat) in user[key].items():
            for (diffItem,diffRat) in deviations.items():
                if diffItem not in user[key] and item in deviations[diffItem]:
                    recommend.setdefault(diffItem,0)
                    freq.setdefault(diffItem,0)
                    recommend[diffItem] += (diffRat[item] + rat) * frequemcies[diffItem][item]
                    freq[diffItem] += frequemcies[diffItem][item]          
        for (k,v) in recommend.items():
            recommendations.setdefault(k,v / freq[k] )
    return recommendations
  
