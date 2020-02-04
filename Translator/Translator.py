# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:22:29 2020

@author: HjYe
"""
import os
import re
from abc import ABCMeta, abstractmethod

from TypeAnalyst import TypeAnalyst

class Translator:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.file_suffix=''
        
    def translate_folder(self, folder_path):
        files = os.listdir(folder_path)
        files_path = [os.path.join(folder_path, f) for f in files]
        cfgs = []
        for file_path in files_path:
            suffix = file_path.split('.')[-1]
            if suffix != self.file_suffix:
                continue
            cfg = self.translate_file(file_path)
            cfgs.append(cfg)
        cfgs = self.confirm_type(cfgs)
        cfgs = self.convert_value(cfgs)
        return cfgs
            
    def translate_file(self, file_path):
        file = open(file_path, 'r')
        items = self.extract_items(file)
        cfg = {}
        for item in items:
            self.append_cfg_item(cfg, item)
        file.close()
        return cfg
    
    @abstractmethod
    def extract_items(self, file):
        return []
    
    @abstractmethod
    def append_cfg_item(self, cfg, item):
        return cfg
    
    def confirm_type(self, cfgs):
        cached_key = dict()
        for cfg in cfgs:
            keys = cfg.keys()
            for key in keys:
                if key in cached_key.keys():
                    type_str = cached_key[key]
                else:
                    type_str = TypeAnalyst.analysis_type(cfgs, key)
                    cached_key[key] = type_str
                cfg[key]['type'] =type_str
        return cfgs
    
    def convert_value(self, cfgs):
        for cfg in cfgs:
            keys = cfg.keys()
            for key in keys:
                if cfg[key]['type'] == 'int':
                    cfg[key]['value'] = int(cfg[key]['value'])
                if cfg[key]['type'] == 'size':
                    value = cfg[key]['value']
                    cfg[key]['value'] = int(re.split("\D+", value)[0])
        
        return cfgs
    
        