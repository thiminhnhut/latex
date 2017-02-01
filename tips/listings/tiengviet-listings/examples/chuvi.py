#!/usr/bin/python
# -*- coding: utf-8 -*-

import math # Thư viện Toán trong Python

def chuvi(rad):
	""" Tính chu vi đường tròn """
	CV = 2*math.pi*rad
	return CV

R = [2, 3, 4, 5]  # Bán kính của đường tròn
for r in R:
	print chuvi(r)	# In ra chu vi của đường tròn
