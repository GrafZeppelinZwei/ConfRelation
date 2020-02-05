# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:53:13 2020

@author: 51974
"""
import re
from Rule.Rule import Rule

class TypeRule(Rule):
    patterns = {'int': [re.compile('^\d+$'),],
                'size': [re.compile('^\d+(([K|M|G|T]B?)|B)$'),],
                'path': [re.compile(r'^[a-zA-Z]:(((\\{1,2}(?! )[^/:*?<>\""|\\]+)+\\?)|(\\)?)\s*$'),
                                 re.compile(r'^(\/([0-9a-zA-Z_.\-]+))+$')]}
    
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
        sentence = "%s should be type of %s, confidence: %f, support: %f"% \
         (self.subj, self.objs[0], self.confidence, self.support)
        print(sentence)
    
    def is_typeof(type_str, value):
        patterns = TypeRule.patterns[type_str]
        print(type_str, value)
        for pattern in patterns:
            if pattern.match(value) != None:
                return True
        return False
        
    def all_type():
        return TypeRule.patterns.keys()
    
    def convert_value(type_str, value):
        if type_str == 'int':
            if TypeRule.is_typeof('int', value):
                value = int(value)
            else:
                value = None
        if type_str == 'size':
            if TypeRule.is_typeof('size', value):
                value = int(re.split("\D+", value)[0])
            else:
                value = None
        return value
    