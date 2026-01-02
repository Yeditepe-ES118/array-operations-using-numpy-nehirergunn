# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 17:58:41 2026

@author: aergu
"""

import numpy as np

def stat():
    data = np.loadtxt("populations.txt")

    # columns: Year, Hare, Lynx, Carrot
    year = data[:, 0]
    hare = data[:, 1]
    lynx = data[:, 2]
    carrot = data[:, 3]

    # year where hare is minimum (actual year, not index)
    min_year_hare = year[np.argmin(hare)]

    # average of lynx
    lynx_avg = np.mean(lynx)

    # total of species ONLY (exclude year)
    total = hare + lynx + carrot

    # add last column
    new_data = np.column_stack((data, total))

    # set carrot < 40000 to 0 (in new_data)
    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data
