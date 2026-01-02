# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 17:58:41 2026

@author: aergu
"""

import numpy as np

def stat():
    data = np.loadtxt("populations.txt")

    hare = data[:, 1]

    min_year_hare = np.argmin(hare)

    lynx_avg = np.mean(data[:, 2])

    total = np.sum(data, axis=1)
    new_data = np.column_stack((data, total))

    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data
