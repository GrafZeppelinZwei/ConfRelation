# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:16:05 2020

@author: 51974
"""

def all_keys(data):
    keys = set()
    for record in data:
        for key in record.keys():
            keys.add(key)
    return keys