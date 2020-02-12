# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:36:13 2020

@author: 51974
"""
#import sys
#sys.path.append("..")
from Rule.RuleFactory import RuleFactory
from Rule.TypeRule import TypeRule
class ConfVertice:
    def __init__(self, name, degree = 0):
        self.name = name
        self.degree = degree
    
    def display(self):
        print(self.name+":", self.degree)
        
class ConfEdge:
    def __init__(self, src_vrt, dst_vrt, weight, class_type):
        self.src_vrt = src_vrt
        self.dst_vrt = dst_vrt
        self.weight = weight
        self.class_type = class_type
        
    def display(self):
        print(self.src_vrt.name, "->", self.dst_vrt.name, self.weight)
    
class ConfGraph:
    def __init__(self, rules):
        self.vrts = {}
        self.edges = {}
        for rule in rules:
            src_vrt = self.get_vrt(rule.subj)
            weight = rule.confidence
            class_type = rule.__class__
            if class_type  == TypeRule:
                dst_vrt = src_vrt
            else:
                dst_vrt = self.get_vrt(rule.objs[0])
            edge = ConfEdge(src_vrt, dst_vrt, weight, class_type)
            self.edges[src_vrt.name].append(edge)
        self.compute_degrees()
                
    def get_vrt(self, vrt_name):
        if vrt_name in self.vrts.keys():
            return self.vrts[vrt_name]
        else:
            vrt = ConfVertice(vrt_name)
            self.vrts[vrt_name] = vrt
            self.edges[vrt_name] = []
            return vrt
    
    def compute_degrees(self):
        for edges in self.edges.values():
            for edge in edges:
                edge.src_vrt.degree += edge.weight
                edge.dst_vrt.degree += edge.weight
    
    def display(self):
        print('vertices:')
        for vrt in self.vrts.values():
            vrt.display()
        print('edges:')
        for edges in self.edges.values():
            for edge in edges:
                edge.display()
    
    def compute_importance(self, rule):
        vrt_num = len(rule.objs)+1
        src_vrt = self.get_vrt(rule.subj)
        tot_degree = src_vrt.degree
        for obj in rule.objs:
            dst_vrt = self.get_vrt(obj)
            tot_degree += dst_vrt.degree
        importance = 1.*tot_degree/vrt_num
        return importance
    
if __name__ == "__main__":
    import json
    file = open("../tests/rules.json")
    rules_json = file.read()
    rules_json = json.loads(rules_json)
    all_rules = []
    for rules in rules_json:
        rule_type = rules['name']
        for rule in rules['rules']:
            rule_obj = RuleFactory.build_rule(rule_type, json = rule)
            all_rules.append(rule_obj)
    graph = ConfGraph(all_rules)
    graph.display()
    all_rules[1].display()
    print(graph.compute_importance(all_rules[1]))
    