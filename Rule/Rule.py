# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:20:14 2020

@author: HjYe
"""
from abc import ABCMeta, abstractmethod

class Rule:
    __metaclass__ = ABCMeta
    
    def __init__(self, subj, objs, support = 0, confidence = 0):
        self.subj = subj
        self.objs = objs
        self.support = support
        self.confidence = confidence
    
    def analysis_record_type(self, record):
        if self.appearance(record):
            if self.satisfy(record):
                return 'support'
            else:
                return 'obey'
        else:
            return None
            
    @abstractmethod
    def appearance(self, record):
        return False
    
    @abstractmethod
    def satisfy(self, record):
        return False
    
    @abstractmethod
    def display(self, record):
        return ""