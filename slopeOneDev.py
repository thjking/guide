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
            print deviations
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