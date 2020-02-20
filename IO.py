# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:57:34 2020

@author: HjYe
"""

import argparse
import yaml
import sys
import json

class Input:
    def __init__(self):
        cfg = self.parse_arg()
        cfg_path = cfg['cfg_path']
        if cfg_path != None:
            cfg = self.load_config(cfg_path)
            
        self.folder_path = cfg['folder_path']
        self.cfg_type = cfg['cfg_type']
        self.spt_thresh = float(cfg['spt_thresh'])
        self.cfd_thresh = float(cfg['cfd_thresh'])
        self.learner_flags = self.init_learner_flags(cfg)
        self.output_path = cfg['output_path']
            
    def load_config_from(self, cfg_path):
        file=open(cfg_path)
        cfg=yaml.load(file)
        file.close()
        return cfg
    
    def init_learner_flags(self, cfg):
        learner_flags = {}
        learner_flags['missing'] = cfg['enablemissing']
        learner_flags['value'] = cfg['enablevalue']
        learner_flags['type'] = cfg['enabletype']
        if learner_flags['value']:
            learner_flags['type'] = True
        return learner_flags
        
    def parse_arg(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--cfg_path', action='store', default=None)
        parser.add_argument('--folder_path', action='store', default=None)
        parser.add_argument('--output_path', action='store', default=None)
        parser.add_argument('--cfg_type', action='store', default='csv')
        parser.add_argument('--spt_thresh', action='store', default=0.1)
        parser.add_argument('--cfd_thresh', action='store', default=0.98)
        parser.add_argument('--enablemissing', action='store_true', default=False)
        parser.add_argument('--enablevalue', action='store_true', default=False)
        parser.add_argument('--enabletype', action='store_true', default=True)
        args=parser.parse_args(sys.argv[1:])
        return vars(args)
    
def parse_input():
    args=Input()
    return args

def display(all_rules):
    for rules in all_rules:
        print(rules['name']+" rules:")
        rules['rules'].sort(reverse = True)
        for rule in rules['rules']:
            rule.display()
            
def to_json(all_rules):
    jsons = json.dumps(all_rules,default = lambda obj: obj.__dict__)
    return jsons

def output(file_path, all_rules):
    json = to_json(all_rules)
    file = open(file_path, 'w')
    file.write(str(json))
    file.close()
    
if __name__ == '__main__':
    args=Input()
    print(args.learner_flags)
        

