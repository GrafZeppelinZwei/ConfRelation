# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:52:32 2020

@author: 51974
"""

class ConfigItem:
    def __init__(self, key, value, type_str = None):
        self.key = key
        self.value = value
        self.type_str = type_str
        
class ConfigRecord:
    def __init__(self, items = {}):
        self.items = items
        self.items_list = [items[key] for key in items.keys()]
        
    def append(self, item):
        key = item.key
        if key not in self.items.keys():
            self.items_list.append(item)
        self.items[key] = item
    
    def keys(self):
        return self.items.keys()
        
class ConfigData:
    def __init__(self, records = []):
        self.records = []
        
    def all_keys(self):
        keys = set()
        for record in self.records:
            for key in record.items.keys():
                keys.add(key)
        return keys