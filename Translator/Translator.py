# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:22:29 2020

@author: HjYe
"""
import os
from abc import ABCMeta, abstractmethod

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
        return cfgs
            
    def translate_file(self, file_path):
        file = open(file_path, 'r',encoding = 'utf-8')
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
    
        