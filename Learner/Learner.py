# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:33:58 2020

@author: HjYe
"""
from abc import ABCMeta, abstractmethod

class Learner:
    __metaclass__ = ABCMeta
    
    def __init__(self, spt_thresh, cfd_thresh):
        self.spt_thresh = spt_thresh
        self.cfd_thresh = cfd_thresh
        self.depth = -1
        self.rule_type = ''
        
    def learn(self, data):
        depth = 0
        all_rules = []
        rules = []
        while depth <= self.depth:
            unchecked = self.gen_rules(rules, data, depth)
            rules = []
            for rule in unchecked:
                record_type_count = self.collect_record_type(
                        rule, data, 'analysis_record_type')
                support, confidence = self.compute_metrics(record_type_count)
                if support > self.spt_thresh:
                    rule.confidence = confidence
                    rule.support = support
                    rules.append(rule)
                    all_rules.append(rule)
            depth += 1
        all_rules =  self.filter_rules(all_rules)
        return {'name': self.rule_type, 'rules': all_rules}
    
    @abstractmethod
    def gen_rules(self, rules, data, depth):       
        return []
        
    def filter_rules(self, rules):
        filtered = []
        for rule in rules:
            if rule.confidence>=self.cfd_thresh:
                filtered.append(rule)
        return filtered                    
    
    def collect_record_type(self, rule, data, method):
        tot_count = len(data)
        record_type_count = {'total': tot_count}
        for record in data:
            func = getattr(rule, method)
            record_type = func(record)
            if record_type == None:
                continue
            if record_type in record_type_count.keys():
                record_type_count[record_type] += 1
            else:
                record_type_count[record_type] = 1
        return record_type_count

    def compute_metrics(self, record_type_count):
        support_count = record_type_count['support'] \
            if 'support' in record_type_count.keys() else 0
        obey_count = record_type_count['obey'] \
            if 'obey' in record_type_count.keys() else 0 
        tot_count = record_type_count['total']
        
        support =1.*support_count/tot_count
        if support_count+obey_count == 0:
            confidence = 0
        else:
            confidence = 1.*support_count/(support_count+obey_count)
        return support, confidence
    