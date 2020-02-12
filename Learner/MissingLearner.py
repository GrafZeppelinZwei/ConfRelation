# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:18:20 2020

@author: HjYe
"""
from Learner.Learner import Learner
from Rule.MissingRule import MissingRule
from utils import all_keys

class MissingLearner(Learner):
    def __init__(self, spt_thresh, cfd_thresh):
        Learner.__init__(self, spt_thresh, cfd_thresh)
        self.depth = 1
        self.rule_type = 'missing'
        
    def gen_rules(self, rules, data, depth):
        new_rules = []
        if depth == 0:
            keys = all_keys(data)
            for key in keys:
                rule = MissingRule(None, [key,])
                new_rules.append(rule)
        elif depth == 1:
            for subj_record in rules:
                for obj_record in rules:
                    subj = subj_record.objs[0]
                    obj = obj_record.objs[0]
                    if subj == obj:
                        continue
                    else:
                        rule = MissingRule(subj, [obj,])
                        new_rules.append(rule)
        else:
            ind = 1
            for rule1 in rules:
                for rule2 in rules[ind:]:
                    if rule1.subj == rule2.subj and \
                     rule1.objs[:-1] == rule2.objs[:-1]:
                         objs = rule1.objs.copy()
                         objs.append(rule2.objs[-1])
                         rule = MissingRule(rule1.subj, objs)
                         new_rules.append(rule)
                ind += 1
        return new_rules
    