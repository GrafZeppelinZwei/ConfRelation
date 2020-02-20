# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:13:57 2020

@author: 51974
"""

from Rule.Rule import Rule

class ValueRule(Rule): 
    def __init__(self, subj, objs, support = 0, confidence = 0, importance = 0, value_relation = ''):
        Rule.__init__(self, subj, objs, support, confidence, importance)
        self.value_relation = value_relation
        
    def appearance(self, record):
        if not self.subj in record.keys():
            return False
        elif record[self.subj]['value'] == None:
            return False
        for obj in self.objs:
            if not obj in record.keys():
                return False
            elif record[obj]['value'] == None:
                return False
        return True
    
    def satisfy(self, record):
        if not self.appearance(record):
            return True
        subj_value = record[self.subj]['value']
        objs_value = [ record[obj]['value'] for obj in self.objs]
        for obj_value in objs_value:
            if not self.value_satisfy(subj_value, objs_value):
                return False
        return True
    
    def display(self):
        sentence = "value of %s should %s values of %s, confidence: %f, support: %f, importance: %f" \
          %(self.subj, self.value_relation, self.objs, self.confidence, self.support, self.importance)
        print(sentence)
        
    def value_satisfy(self, subj_value, objs_value):
        for obj_value in objs_value:
            if self.value_relation == '<' and not subj_value < obj_value:
                return False
            if self.value_relation == '=' and not subj_value == obj_value:
                return False
            if self.value_relation == '>' and not subj_value > obj_value:
                return False
            if self.value_relation == '<=' and not subj_value <= obj_value:
                return False
            if self.value_relation == '>=' and not subj_value >= obj_value:
                return False
        return True
    
    def analysis_value_relation(self, record):
        if not self.appearance(record):
            return None
        subj_value = record[self.subj]['value']
        obj_value = record[self.objs[0]]['value']
        if subj_value < obj_value:
            return '<'
        elif subj_value == obj_value:
            return '='
        else:
            return '>'