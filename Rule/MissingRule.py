# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:24:33 2020

@author: HjYe
"""

from Rule.Rule import Rule

class MissingRule(Rule):        
    def appearance(self, record):
        keys = record.keys()
        if self.subj in keys or self.subj == None:
            return True
        else:
            return False
        
    def satisfy(self, record):
        keys = record.keys()
        if not self.appearance(record):
            return False
        for obj in self.objs:
            if not obj in keys:
                return False
        return True
    
    def display(self):
        sentence = "when %s appear, %s should appear. confidence: %f, support: %f" \
          %(self.subj, self.objs, self.confidence, self.support)
        print(sentence)