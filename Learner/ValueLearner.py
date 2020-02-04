# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:34:07 2020

@author: 51974
"""

from Learner.Learner import Learner
from Rule.ValueRule import ValueRule

class ValueLearner(Learner):
    def __init__(self, spt_thresh, cfd_thresh):
        Learner.__init__(self, spt_thresh, cfd_thresh)
        self.depth = 1
        self.rule_type = 'value'
        
    def gen_rules(self, rules, data, depth):
        new_rules = []
        keys = set()
        for record in data:
            for key in record.keys():
                if record[key]['type'] not in ['int', 'size']:
                    continue
                keys.add(key)
        keys = list(keys)
        if depth == 1:
            ind = 1
            for subj in keys:
                for obj in keys[ind:]:
                    rule = ValueRule(subj, [obj,])
                    new_rules.append(rule)
                ind += 1
        return new_rules
    
    def learn(self, data):
        all_rules = []
        rules = self.gen_rules(None, data, 1)
        for rule in rules:
            value_relation_count = self.collect_record_type(rule,
                                    data, 'analysis_value_relation')
            value_relation = self.confirm_value_relation(value_relation_count)
            rule.value_relation = value_relation
            record_type_count = self.collect_record_type(rule, 
                                    data, 'analysis_record_type')
            support, confidence = self.compute_metrics(record_type_count)
            if support > self.spt_thresh:
                rule.confidence = confidence
                rule.support = support
                all_rules.append(rule)
        
        all_rules =  self.filter_rules(all_rules)
        return {'name': self.rule_type, 'rules': all_rules}
    
    def confirm_value_relation(self, value_relation_count):
        if '<' not in value_relation_count.keys():
            value_relation_count['<'] = 0
        if '=' not in value_relation_count.keys():
            value_relation_count['='] = 0
        if '>' not in value_relation_count.keys():
            value_relation_count['>'] = 0
        value_relation_count.pop('total')
        if None in value_relation_count.keys():
            value_relation_count.pop(None)
                    
        value_relation_count['<='] = value_relation_count['<']+value_relation_count['=']
        value_relation_count['>='] = value_relation_count['>']+value_relation_count['=']
        max_count = max(value_relation_count.values())
        for k, v in value_relation_count.items():
            if v == max_count:
                value_relation = k
                break
        if value_relation == '<=' and value_relation_count['='] == 0:
            value_relation = '<'
        if value_relation == '>=' and value_relation_count['='] == 0:
            value_relation = '>'
        return value_relation
                    
                    
                    
                    
                    