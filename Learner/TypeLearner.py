# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:07:22 2020

@author: 51974
"""
import re

from Learner.Learner import Learner
from Rule.TypeRule import TypeRule
class TypeLearner(Learner):
    def __init__(self, spt_thresh, cfd_thresh):
        Learner.__init__(self, spt_thresh, cfd_thresh)
        self.depth = 1
        self.rule_type = 'type'
        
    def gen_rules(self, rules, data, depth):
        rules = []
        if depth != 1:
            return rules

        keys = set()
        for record in data:
            for key in record.keys():
                keys.add(key)
        
        all_type =TypeRule.all_type()
        for key in keys:
            for type_str in all_type:
                rule = TypeRule(key, [type_str,])
                rules.append(rule)
        return rules
    
    def learn(self, data):
        result = Learner.learn(self, data)
        rules = result['rules']
        self.post_processing(rules, data)
        return result
    
    def post_processing(self, rules, data):
        for rule in rules:
            type_str = rule.objs[0]
            for record in data:
                if rule.subj in record.keys():
                    record[rule.subj]['type'] = type_str
                    value = record[rule.subj]['value']
                    record[rule.subj]['value'] = TypeRule.convert_value(type_str, value)
        return data
    
                    
                    
                    