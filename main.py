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
print a 