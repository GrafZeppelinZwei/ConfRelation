# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:41:31 2020

@author: HjYe
"""
import json
import argparse
import sys

from Rule.RuleFactory import RuleFactory
from Rule.TypeRule import TypeRule
from Translator.TranslatorFactory import TranslatorFactory

class Checker:
    def __init__(self, file_path):
        file = open(file_path)
        rules_json = file.read()
        self.all_rules = json.loads(rules_json)
        self.rulesjson2obj()
        self.fails = []
        file.close()
        
    def check(self, record):
        self.fails = []
        for rules in self.all_rules:
            for rule in rules['rules']:
                appearance_type = rule.analysis_record_type(record)
                if appearance_type == 'obey':
                    self.fails.append(rule)
                if rule.__class__ ==TypeRule and \
                    rule.subj in record.keys():
                    value = record[rule.subj]['value']
                    record[rule.subj]['value'] = TypeRule.convert_value(rule.objs[0], value)
        return self.fails
    
    def display(self):
        for rule in self.fails:
            rule.display()
     
    def rulesjson2obj(self):
        for rules in self.all_rules:
            rules_obj = []
            rule_type = rules['name']
            for rule in rules['rules']:
                rule_obj = RuleFactory.build_rule(rule_type, json = rule)
                rules_obj.append(rule_obj)
            rules['rules'] = rules_obj

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', action='store', default=None)
    parser.add_argument('--rule_path', action='store', default=None)
    parser.add_argument('--cfg_type', action='store', default='csv')
    args=parser.parse_args(sys.argv[1:])
    return vars(args)

if __name__ == "__main__":
    args = parse_arg()
    translator = TranslatorFactory.build_translator(args['cfg_type'])
    record = translator.translate_file(args['file_path'])
    #record = translator.confirm_type([record,])[0]
    #record = translator.convert_value([record,])[0]
    for k,v in record.items():
        print(k, ":", v)
    checker = Checker(args['rule_path'])
    checker.check(record)
    checker.display()