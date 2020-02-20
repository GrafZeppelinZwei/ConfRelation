# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:30:32 2020

@author: HjYe
"""

from Rule.MissingRule import MissingRule
from Rule.ValueRule import ValueRule
from Rule.TypeRule import TypeRule

class RuleFactory:
    def build_rule(type_str, subj = None, objs = [], support = 0, confidence = 0, importance = 0, json = None):
        if json != None:
            subj = json['subj']
            objs = json['objs']
            support = json['support']
            confidence = json['confidence']
            importance = json['importance']
            
        if type_str == 'missing':
            rule = MissingRule(subj, objs, support, confidence, importance)
        elif type_str == 'value':
            if json != None:
                value_relation = json['value_relation']
            rule = ValueRule(subj, objs, support, confidence, importance, value_relation)
        elif type_str == 'type':
            rule = TypeRule(subj, objs, support, confidence, importance)
        else:
            rule = None
        return rule