# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:53:13 2020

@author: 51974
"""
import re
from Rule.Rule import Rule

class TypeRule(Rule):
    types = ['int', 'size', 'path', 'bool', 'ipaddr']
    
    def appearance(self, record):
        if self.subj in record.keys():
            return True
        else:
            return False
    
    def satisfy(self, record):
        if not self.appearance(record):
            return True
        value = record[self.subj]['value']
        type_str = self.objs[0]
        if TypeRule.is_typeof(type_str, value):
            return True
        else:
            return False
    
    def display(self):
        sentence = "%s should be type of %s, confidence: %f, support: %f, importance: %f"% \
         (self.subj, self.objs[0], self.confidence, self.support, self.importance)
        print(sentence)
    
    def is_typeof(type_str, value):
        func_name = 'is_'+type_str
        func = getattr(TypeRule, func_name)
        return func(value)
    
    def is_int(value):
        pattern = re.compile('^\d+$')
        if pattern.match(value) != None:
            return True
        else:
            return False
        
    def is_size(value):
        pattern = re.compile('^\d+(([K|M|G|T]B?)|B)$')
        if pattern.match(value) != None:
            return True
        else:
            return False
    
    def is_path(value):
        patterns = [re.compile(r'^[a-zA-Z]:(((\\{1,2}(?! )[^/:*?<>\""|\\]+)+\\?)|(\\)?)\s*$'),
                                 re.compile(r'^(\/([0-9a-zA-Z_.\-]+))+$')]
        for pattern in patterns:
            if pattern.match(value) != None:
                return True
        return False
    
    def is_bool(value):
        pattern = re.compile('^(True|False|ON|OFFF)$', re.I)
        if pattern.match(value) != None:
            return True
        else:
            return False
    
    def is_ipaddr(value):
        pattern = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        if pattern.match(value) == None:
            return False
        nums = value.split('.')
        for num in nums:
            if int(num)<0 or int(num)>255:
                return False
        return True
    
    def all_type():
        return TypeRule.types
    
    def convert_value(type_str, value):
        if type_str == 'int':
            if TypeRule.is_typeof('int', value):
                value = int(value)
            else:
                value = None
        if type_str == 'size':
            if TypeRule.is_typeof('size', value):
                size = (re.split("\D+",value))[1]
                value = int(re.split("\D+", value)[0])
                if size == 'K' or size == 'KB':
                    value *= 1024
                if size == 'M' or size == 'MB':
                    value *= 1024*1024
                if size == 'G' or size == 'GB':
                    value *= 1024*1024*1024
            else:
                value = None
        return value
    
