# -*- coding:UTF-8 -*-
from math import sqrt
from data import users,users2,users3,loadMovieLens
import manhattan as mh
import Minkowski as mk
import pearson as ps
import computeSimilarity as cp
import normalization as nm
import predict as pd
import slopeOneDev as so
a = loadMovieLens('ratings.csv')
b = so.slopeOneRecommendtions(a,a['1'])
print sorted(b.items(),key = lambda item:item[1])
